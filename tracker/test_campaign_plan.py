import contextlib
import copy
import gzip
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import campaign_plan as planner
import canonical_cut


def module(number, imports=()):
    return dict(id=f'M{number:06}', imports=[f'M{n:06}' for n in imports])


def group(task, targets, modules):
    return dict(task=task, targets=[f'M{n:06}' for n in targets],
                modules=[f'M{n:06}' for n in modules])


def campaign(groups):
    pins = planner.evidence.pins()
    return dict(lean=pins['lean'], lean_commit=pins['commit'], mathlib=pins['mathlib'],
                input_manifest_sha256=pins['inputs_manifest_sha256'], task_count=len(groups),
                distinct_module_ids=len({m for g in groups for m in g['modules']}), workers=groups)


class CampaignPlanTests(unittest.TestCase):
    def setUp(self):
        self.rows = [module(1), module(2, [1]), module(3, [1]), module(4, [2, 3])]
        self.groups = [group(1, [4], [1, 2, 3, 4]), group(2, [2], [1, 2]), group(3, [3], [1, 3])]

    def test_diamond_shared_import_is_counted_once_per_persistent_worker(self):
        result = planner.compare(campaign(self.groups), self.rows, [1], include_assignments=True)
        comparison = result['comparisons'][0]
        self.assertTrue(result['campaign']['project_import_closures_verified'])
        self.assertEqual(comparison['cold_lpt']['total_compile_proxy'], 8)
        self.assertEqual(comparison['cold_lpt']['max_worker_compile_proxy'], 8)
        self.assertEqual(comparison['persistent']['total_compile_proxy'], 4)
        self.assertEqual(comparison['persistent']['max_worker_compile_proxy'], 4)
        self.assertTrue(comparison['persistent']['all_groups_exactly_once'])
        self.assertTrue(comparison['persistent']['requested_target_coverage_exact'])
        self.assertEqual(comparison['persistent']['assignments'][0]['groups'], [1, 2, 3])

    def test_overlap_saves_work_while_balancing_the_same_two_workers(self):
        rows = [module(1)] + [module(n, [1]) for n in range(2, 10)]
        groups = [group(n - 1, [n], [1, n]) for n in range(2, 10)]
        result = planner.compare(campaign(groups), rows, [2], include_assignments=True)['comparisons'][0]
        self.assertEqual(result['cold_lpt']['total_compile_proxy'], 16)
        self.assertEqual(result['cold_lpt']['max_worker_compile_proxy'], 8)
        warm = result['persistent']
        self.assertEqual(warm['total_compile_proxy'], 10)
        self.assertEqual(warm['max_worker_compile_proxy'], 5)
        self.assertEqual(warm['active_workers'], 2)
        self.assertEqual(warm['imbalance_max_over_mean'], 1)
        self.assertEqual([len(w['groups']) for w in warm['assignments']], [4, 4])

    def test_disjoint_groups_have_no_artificial_cache_savings(self):
        rows = [module(n) for n in range(1, 9)]
        groups = [group(n, [n], [n]) for n in range(1, 9)]
        result = planner.compare(campaign(groups), rows, [2])['comparisons'][0]
        self.assertEqual(result['cold_lpt']['total_compile_proxy'], 8)
        self.assertEqual(result['persistent']['total_compile_proxy'], 8)
        self.assertEqual(result['cold_lpt']['max_worker_compile_proxy'], 4)
        self.assertEqual(result['persistent']['max_worker_compile_proxy'], 4)
        self.assertEqual(result['compile_proxy_reduction_fraction'], 0)

    def test_largest_first_does_not_send_every_group_to_one_cached_worker(self):
        rows = [module(1), module(2, [1]), module(3, [2])]
        groups = [group(1, [1], [1]), group(2, [3], [1, 2, 3])]
        result = planner.compare(campaign(groups), rows, [2], include_assignments=True)['comparisons'][0]
        # Sending both groups to worker zero would minimize total work, but
        # ignores that worker one's smaller group can finish earlier.
        self.assertEqual(result['persistent']['active_workers'], 2)
        self.assertEqual([w['groups'] for w in result['persistent']['assignments']], [[2], [1]])
        self.assertEqual([w['compile_proxy'] for w in result['cold_lpt']['assignments']], [3, 1])

    def test_multi_target_and_repeated_target_requests_are_preserved(self):
        groups = [group(1, [2, 3], [1, 2, 3]), group(2, [2], [1, 2])]
        result = planner.compare(campaign(groups), self.rows, [1], include_assignments=True)
        self.assertEqual(result['campaign']['requested_target_occurrences'], 3)
        self.assertEqual(result['campaign']['distinct_requested_targets'], 2)
        warm = result['comparisons'][0]['persistent']
        self.assertEqual(warm['groups_assigned'], 2)
        self.assertEqual(warm['requested_targets_assigned'], 3)
        self.assertEqual(warm['assignments'][0]['targets'], ['M000002', 'M000003', 'M000002'])

    def test_plan_is_deterministic_when_input_records_are_reordered(self):
        original = planner.compare(campaign(self.groups), self.rows, [1, 2])
        reversed_input = planner.compare(campaign(list(reversed(self.groups))), list(reversed(self.rows)), [1, 2])
        self.assertEqual(original, reversed_input)

    def test_unknown_ids_and_incomplete_or_extra_closure_members_are_rejected(self):
        for modules, message in (([1, 2, 3, 999], 'unknown modules'),
                                 ([2, 3, 4], 'differs from target import closure'),
                                 ([1, 2, 3, 4, 5], 'differs from target import closure')):
            with self.subTest(modules=modules):
                groups = [group(1, [4], modules)]
                with self.assertRaisesRegex(ValueError, message):
                    planner.compare(campaign(groups), self.rows + [module(5)], [1])
        groups = [group(1, [999], [1])]
        with self.assertRaisesRegex(ValueError, 'unknown targets'):
            planner.compare(campaign(groups), self.rows, [1])

    def test_duplicate_groups_modules_and_targets_are_rejected(self):
        invalid = [self.groups + [self.groups[0]],
                   [group(1, [2], [1, 1, 2])], [group(1, [2, 2], [1, 2])]]
        for groups in invalid:
            with self.subTest(groups=groups), self.assertRaises(ValueError):
                planner.compare(campaign(groups), self.rows, [1])

    def test_worker_bounds_and_campaign_metadata_are_validated(self):
        for counts in ([0], [-1], [4], [True], [1.5], [], [1, 1]):
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                planner.compare(campaign(self.groups), self.rows, counts)
        for key, value in (('lean', 'bad'), ('task_count', 99), ('distinct_module_ids', 99)):
            data = campaign(self.groups)
            data[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                planner.compare(data, self.rows, [1])

    def test_cli_reads_existing_compressed_campaign_without_mutating_inputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'campaign.json.gz'
            data = campaign(self.groups)
            original = copy.deepcopy(data)
            with gzip.open(path, 'wt') as stream:
                json.dump(data, stream)
            before = path.read_bytes()
            with patch.object(planner.tasks, 'module_rows', return_value=iter(self.rows)), \
                    contextlib.redirect_stdout(io.StringIO()) as output:
                code = planner.main([str(path), '--workers', '1', '2', '--include-assignments'])
            result = json.loads(output.getvalue())
            self.assertEqual(code, 0)
            self.assertEqual([r['workers'] for r in result['comparisons']], [1, 2])
            self.assertEqual(result['input']['sha256'], planner.tasks.digest(path))
            self.assertNotIn(temporary, json.dumps(result))
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(data, original)
            with patch.object(planner.tasks, 'module_rows', return_value=iter(self.rows)), \
                    contextlib.redirect_stdout(io.StringIO()) as output:
                code = planner.main([str(path), '--workers', '0'])
            self.assertEqual(code, 2)
            self.assertEqual(json.loads(output.getvalue())['status'], 'invalid')


class CanonicalCutTests(unittest.TestCase):
    def test_shared_prefix_has_one_producer_with_balanced_private_work(self):
        rows = [module(1)] + [module(n, [1]) for n in range(2, 10)]
        groups = [group(n - 1, [n], [1, n]) for n in range(2, 10)]
        result = planner.compare(campaign(groups), rows, [2], include_assignments=True,
                                 canonical_cut=True)['comparisons'][0]['canonical_cut']
        self.assertEqual(result['seed_module_ids'], ['M000001'])
        self.assertEqual(result['total_compile_proxy'], 9)
        self.assertEqual(result['private_compile_proxies'], [4, 4])
        self.assertEqual(result['seed_object_deliveries'], 2)
        self.assertEqual(result['unit_model']['two_stage_rounds'], 5)
        self.assertTrue(result['each_module_has_one_producer'])
        self.assertTrue(result['all_groups_exactly_once'])
        private = [m for worker in result['assignments'] for m in worker['private_module_ids']]
        self.assertEqual(len(private), len(set(private)))
        self.assertEqual(set(private) | set(result['seed_module_ids']), {r['id'] for r in rows})

    def test_diamond_seed_is_dependency_closed_and_waits_for_inputs(self):
        rows = [module(1), module(2, [1]), module(3, [1]), module(4, [2, 3])]
        groups = [group(1, [4], [1, 2, 3, 4]), group(2, [2], [1, 2]), group(3, [3], [1, 3])]
        result = planner.compare(campaign(groups), rows, [2], include_assignments=True,
                                 canonical_cut=True)['comparisons'][0]['canonical_cut']
        self.assertEqual(result['seed_module_ids'], ['M000001', 'M000002', 'M000003'])
        self.assertEqual(result['total_compile_proxy'], 4)
        self.assertEqual(result['unit_model']['seed_rounds'], 2)
        self.assertEqual(result['unit_model']['two_stage_rounds'], 3)
        self.assertTrue(result['seed_dependency_closed'])

    def test_disjoint_work_has_no_invented_seed_or_compile_saving(self):
        rows = [module(n) for n in range(1, 9)]
        groups = [group(n, [n], [n]) for n in range(1, 9)]
        result = planner.compare(campaign(groups), rows, [2], canonical_cut=True)['comparisons'][0]
        self.assertEqual(result['cold_lpt']['total_compile_proxy'], 8)
        self.assertEqual(result['canonical_cut']['seed_modules'], 0)
        self.assertEqual(result['canonical_cut']['total_compile_proxy'], 8)
        self.assertEqual(result['canonical_cut']['unit_model']['two_stage_rounds'], 4)
        self.assertNotIn('assignments', result['persistent'])

    def test_private_overlap_components_move_as_indivisible_units(self):
        rows = [module(1), module(2, [1]), module(3, [1]),
                module(4), module(5, [4]), module(6, [4])]
        records = [group(1, [2], [1, 2]), group(2, [3], [1, 3]),
                   group(3, [5], [4, 5]), group(4, [6], [4, 6])]
        groups, _ = planner.prepare(campaign(records), rows)
        warm = {'assignments': [{'groups': [1, 2]}, {'groups': [3, 4]}]}
        result = canonical_cut.plan(groups, warm, sorted(r['id'] for r in rows),
                                    {r['id']: r['imports'] for r in rows}, 2, True)
        self.assertEqual(result['seed_modules'], 0)
        self.assertEqual(result['private_component_count'], 2)
        self.assertEqual(result['private_compile_proxies'], [3, 3])
        assignments = [set(w['groups']) for w in result['assignments']]
        self.assertIn({1, 2}, assignments)
        self.assertIn({3, 4}, assignments)

    def test_all_seed_case_preserves_repeated_target_requests(self):
        rows = [module(1), module(2, [1])]
        groups, _ = planner.prepare(campaign([group(1, [2], [1, 2]),
                                               group(2, [2], [1, 2])]), rows)
        warm = {'assignments': [{'groups': [1]}, {'groups': [2]}]}
        result = canonical_cut.plan(groups, warm, sorted(r['id'] for r in rows),
                                    {r['id']: r['imports'] for r in rows}, 2, True)
        self.assertEqual(result['total_compile_proxy'], 2)
        self.assertEqual(result['private_modules'], 0)
        self.assertEqual(result['private_imbalance_max_over_mean'], 0)
        self.assertEqual(result['unit_model']['two_stage_rounds'], 2)
        self.assertEqual(result['requested_targets_assigned'], 2)
        self.assertTrue(result['requested_target_coverage_exact'])

    def test_unit_schedule_checks_cycles_slots_and_round_boundaries(self):
        imports = {'A': [], 'B': ['A'], 'C': ['B'], 'D': ['C']}
        self.assertEqual(canonical_cut.unit_schedule(imports, imports, 8), (4, 3))
        for slots in (0, -1, True, 1.5):
            with self.subTest(slots=slots), self.assertRaises(ValueError):
                canonical_cut.unit_schedule(imports, imports, slots)
        with self.assertRaisesRegex(ValueError, 'cycle'):
            canonical_cut.unit_schedule({'A', 'B'}, {'A': ['B'], 'B': ['A']}, 2)

    def test_canonical_plan_is_deterministic(self):
        rows = [module(1), module(2, [1]), module(3, [1]), module(4, [2, 3])]
        groups = [group(1, [4], [1, 2, 3, 4]), group(2, [2], [1, 2]), group(3, [3], [1, 3])]
        first = planner.compare(campaign(groups), rows, [1, 2, 3], True, True)
        second = planner.compare(campaign(list(reversed(groups))), list(reversed(rows)),
                                  [1, 2, 3], True, True)
        self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
