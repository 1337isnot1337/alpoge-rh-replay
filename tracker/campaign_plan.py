"""Compare cold LPT and persistent-worker assignment using published module-build sets."""
import argparse
from collections import Counter
from dataclasses import dataclass
import gzip
import hashlib
import json
from pathlib import Path

import replay_evidence as evidence
import tasks


DEFAULT_WORKERS = (8, 16, 32, 64, 128, 500)
ASSUMPTIONS = [
    'Retrospective module-count proxy only: not CPU time, elapsed time, monetary cost or full-proof ETA.',
    'Every group executes once with its original requested targets; no claims or workers are created.',
    'Project build sets must equal the indexed transitive project-import closures of their targets.',
    'All modules have equal modeled cost; each worker executes assigned groups sequentially.',
    'Persistent workers start with empty project caches and retain all compatible project artifacts.',
    'Reuse assumes matching source, toolchain, native platform and dependency provenance; this model does not verify artifact reuse.',
    'Cross-worker transfers, cache limits, Mathlib preparation, failures, task overhead and final verification are excluded.',
]


@dataclass(frozen=True)
class Group:
    task: int
    targets: tuple
    bits: int


def prepare(campaign, rows):
    pins = evidence.pins()
    for expected, field in (('lean', 'lean'), ('commit', 'lean_commit'), ('mathlib', 'mathlib'),
                            ('inputs_manifest_sha256', 'input_manifest_sha256')):
        if campaign.get(field) != pins[expected]:
            raise ValueError('Campaign pin mismatch: ' + field)
    imports = {row['id']: set(row['imports']) for row in rows}
    if not imports or len(imports) != len(rows):
        raise ValueError('Invalid module index IDs')
    workers = campaign.get('workers')
    if (not isinstance(workers, list) or not workers or type(campaign.get('task_count')) is not int
            or campaign['task_count'] != len(workers)):
        raise ValueError('Campaign task count does not match nonempty worker records')
    task_ids = set()
    records = []
    universe = set()
    for worker in workers:
        task = worker.get('task')
        if type(task) is not int or task <= 0 or task in task_ids:
            raise ValueError('Group task IDs must be unique positive integers')
        task_ids.add(task)
        for field in ('modules', 'targets'):
            values = worker.get(field)
            if (not isinstance(values, list) or not values or not all(isinstance(v, str) for v in values)
                    or len(set(values)) != len(values)):
                raise ValueError(f'Group {task}: {field} must be nonempty unique module IDs')
            unknown = set(values) - imports.keys()
            if unknown:
                raise ValueError(f'Group {task}: unknown {field}: ' + ', '.join(sorted(unknown)[:5]))
        closure = set()
        pending = list(worker['targets'])
        while pending:
            module = pending.pop()
            if module not in imports:
                raise ValueError('Unknown indexed import: ' + module)
            if module not in closure:
                closure.add(module)
                pending.extend(imports[module])
        modules = set(worker['modules'])
        if modules != closure:
            raise ValueError(f'Group {task}: observed build set differs from target import closure '
                             f'(missing {len(closure - modules)}, extra {len(modules - closure)})')
        records.append((task, tuple(worker['targets']), modules))
        universe.update(modules)
    if type(campaign.get('distinct_module_ids')) is not int or campaign['distinct_module_ids'] != len(universe):
        raise ValueError('Campaign distinct module count does not match build sets')
    positions = {module: index for index, module in enumerate(sorted(universe))}
    groups = []
    for task, targets, modules in records:
        bits = 0
        for module in modules:
            bits |= 1 << positions[module]
        groups.append(Group(task, targets, bits))
    return sorted(groups, key=lambda group: (-group.bits.bit_count(), group.task)), len(universe)


def assign(groups, worker_count, persistent=False, include_assignments=False):
    if type(worker_count) is not int or not 1 <= worker_count <= len(groups):
        raise ValueError('Worker count must be between 1 and the number of groups')
    loads = [0] * worker_count
    caches = [0] * worker_count
    assignments = [[] for _ in range(worker_count)]
    for group in groups:
        size = group.bits.bit_count()
        if persistent:
            missing = [(group.bits & ~cache).bit_count() for cache in caches]
            worker = min(range(worker_count), key=lambda i:
                         (loads[i] + missing[i], missing[i], len(assignments[i]), i))
            loads[worker] += missing[worker]
            caches[worker] |= group.bits
        else:
            worker = min(range(worker_count), key=lambda i: (loads[i], i))
            loads[worker] += size
        assignments[worker].append(group)
    actual = [group for worker in assignments for group in worker]
    groups_exact = Counter(group.task for group in actual) == Counter(group.task for group in groups)
    targets_exact = (Counter(target for group in actual for target in group.targets)
                     == Counter(target for group in groups for target in group.targets))
    if not groups_exact or not targets_exact:
        raise ValueError('Assignment coverage mismatch')
    total = sum(loads)
    plan_ids = [[group.task for group in worker] for worker in assignments]
    report = dict(total_compile_proxy=total, max_worker_compile_proxy=max(loads),
                  imbalance_max_over_mean=round(max(loads) * worker_count / total, 6),
                  active_workers=sum(bool(worker) for worker in assignments),
                  groups_assigned=len(actual), requested_targets_assigned=sum(len(g.targets) for g in actual),
                  all_groups_exactly_once=groups_exact, requested_target_coverage_exact=targets_exact,
                  assignment_sha256=hashlib.sha256(json.dumps(plan_ids, separators=(',', ':')).encode()).hexdigest())
    if include_assignments:
        report['assignments'] = [dict(worker=index, compile_proxy=loads[index],
            groups=[group.task for group in assigned], targets=[t for g in assigned for t in g.targets])
            for index, assigned in enumerate(assignments)]
    return report


def compare(campaign, rows, worker_counts=None, include_assignments=False):
    groups, distinct = prepare(campaign, rows)
    if worker_counts is None:
        worker_counts = [w for w in DEFAULT_WORKERS if w <= len(groups)] or [len(groups)]
    if not worker_counts or len(set(worker_counts)) != len(worker_counts):
        raise ValueError('Supply distinct worker counts')
    comparisons = []
    for count in worker_counts:
        cold = assign(groups, count, include_assignments=include_assignments)
        warm = assign(groups, count, persistent=True, include_assignments=include_assignments)
        comparisons.append(dict(workers=count, cold_lpt=cold, persistent=warm,
            compile_proxy_reduction_fraction=round(1 - warm['total_compile_proxy'] / cold['total_compile_proxy'], 6),
            max_worker_proxy_reduction_fraction=round(
                1 - warm['max_worker_compile_proxy'] / cold['max_worker_compile_proxy'], 6)))
    targets = [target for group in groups for target in group.targets]
    return dict(scope='Offline persistent-worker assignment counterfactual, not a runtime forecast.',
                campaign=dict(groups=len(groups), requested_target_occurrences=len(targets),
                              distinct_requested_targets=len(set(targets)), distinct_modules=distinct,
                              original_compile_occurrences=sum(group.bits.bit_count() for group in groups),
                              project_import_closures_verified=True),
                assumptions=list(ASSUMPTIONS), comparisons=comparisons)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('campaign', type=Path, help='published campaign JSON or JSON.gz')
    parser.add_argument('--workers', nargs='+', type=int, help='fixed worker counts to compare')
    parser.add_argument('--include-assignments', action='store_true', help='include group/target assignment details')
    args = parser.parse_args(argv)
    try:
        opener = gzip.open if args.campaign.suffix == '.gz' else open
        with opener(args.campaign, 'rt', encoding='utf-8') as stream:
            campaign = json.load(stream)
        report = compare(campaign, list(tasks.module_rows()), args.workers, args.include_assignments)
        report['input'] = dict(name=args.campaign.name, sha256=tasks.digest(args.campaign),
                              lean=campaign['lean'], lean_commit=campaign['lean_commit'],
                              mathlib=campaign['mathlib'], input_manifest_sha256=campaign['input_manifest_sha256'])
    except (OSError, EOFError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(json.dumps(dict(status='invalid', error=str(error))))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
