"""Conceptual single-producer seed/private partition; no artifact execution or transfer."""
from collections import Counter, defaultdict
import hashlib
from heapq import heapify, heappop, heappush
import json


def members(bits, module_ids):
    while bits:
        bit = bits & -bits
        yield module_ids[bit.bit_length() - 1]
        bits ^= bit


def unit_schedule(nodes, imports, slots):
    """Construct unit rounds, admitting newly ready nodes only in the next round."""
    if type(slots) is not int or slots <= 0:
        raise ValueError('Module slots must be a positive integer')
    nodes = set(nodes)
    dependencies = {node: set(imports[node]) & nodes for node in nodes}
    consumers = defaultdict(list)
    for node, deps in dependencies.items():
        for dep in deps:
            consumers[dep].append(node)
    remaining = {node: len(deps) for node, deps in dependencies.items()}
    ready = [node for node, count in remaining.items() if not count]
    heapify(ready)
    depth = {}
    rounds = 0
    while ready:
        batch = [heappop(ready) for _ in range(min(slots, len(ready)))]
        rounds += 1
        for node in batch:
            depth[node] = 1 + max((depth[d] for d in dependencies[node]), default=-1)
        for node in batch:
            for consumer in consumers[node]:
                remaining[consumer] -= 1
                if remaining[consumer] == 0:
                    heappush(ready, consumer)
    if len(depth) != len(nodes):
        raise ValueError('Canonical-cut dependency graph contains a cycle')
    return rounds, max(depth.values(), default=None)


def plan(groups, warm, module_ids, imports, workers, include_assignments=False):
    by_task = {group.task: group for group in groups}
    union = seed = 0
    for worker in warm['assignments']:
        bits = 0
        for task in worker['groups']:
            bits |= by_task[task].bits
        seed |= union & bits
        union |= bits
    seed_ids = set(members(seed, module_ids))
    if any(set(imports[node]) - seed_ids for node in seed_ids):
        raise ValueError('Canonical seed is not dependency-closed')

    # Groups sharing any private module must remain together, or moving them
    # to different workers would silently reintroduce duplicate producers.
    parent = list(range(len(groups)))

    def find(index):
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    owner = {}
    for index, group in enumerate(groups):
        bits = group.bits & ~seed
        while bits:
            bit = bits & -bits
            position = bit.bit_length() - 1
            previous = owner.setdefault(position, index)
            a, b = find(index), find(previous)
            parent[max(a, b)] = min(a, b)
            bits ^= bit
    grouped = defaultdict(list)
    for index, group in enumerate(groups):
        grouped[find(index)].append(group)
    components = []
    for assigned in grouped.values():
        private = full = 0
        for group in assigned:
            full |= group.bits
            private |= group.bits & ~seed
        private_ids = set(members(private, module_ids))
        if any(set(imports[node]) - private_ids - seed_ids for node in private_ids):
            raise ValueError('Private component has a dependency outside itself and the seed')
        unit_schedule(private_ids, imports, 1)  # Validate that serial private execution is possible.
        components.append((private.bit_count(), min(g.task for g in assigned), private, full, assigned))

    loads = [0] * workers
    private_bits = [0] * workers
    full_bits = [0] * workers
    assignments = [[] for _ in range(workers)]
    for size, _, private, full, assigned in sorted(components, key=lambda c: (-c[0], c[1])):
        worker = min(range(workers), key=lambda i: (loads[i], len(assignments[i]), i))
        loads[worker] += size
        private_bits[worker] |= private
        full_bits[worker] |= full
        assignments[worker].extend(assigned)
    seen = seed
    for bits in private_bits:
        if seen & bits:
            raise ValueError('Canonical cut assigned a module to multiple producers')
        seen |= bits
    if seen != union or seed.bit_count() + sum(loads) != union.bit_count():
        raise ValueError('Canonical-cut module coverage mismatch')
    actual = [group for worker in assignments for group in worker]
    groups_exact = Counter(g.task for g in actual) == Counter(g.task for g in groups)
    targets_exact = (Counter(t for g in actual for t in g.targets)
                     == Counter(t for g in groups for t in g.targets))
    if not groups_exact or not targets_exact:
        raise ValueError('Canonical-cut group or target coverage mismatch')
    rounds, seed_depth = unit_schedule(seed_ids, imports, workers)
    deliveries = [(bits & seed).bit_count() for bits in full_bits]
    private_total = sum(loads)
    result = dict(scope='Concept requiring a new canonical artifact store and executor; not measured time or ETA.',
        seed_modules=seed.bit_count(), seed_dependency_closed=True, seed_max_import_depth=seed_depth,
        seed_module_ids_sha256=hashlib.sha256(json.dumps(sorted(seed_ids), separators=(',', ':')).encode()).hexdigest(),
        private_modules=private_total, private_component_count=len(components),
        private_max_worker_compile_proxy=max(loads),
        private_imbalance_max_over_mean=round(max(loads) * workers / private_total, 6) if private_total else 0.0,
        private_compile_proxies=loads, active_private_workers=sum(load > 0 for load in loads),
        total_compile_proxy=seed.bit_count() + private_total, each_module_has_one_producer=True,
        all_groups_exactly_once=groups_exact, requested_target_coverage_exact=targets_exact,
        groups_assigned=len(actual), requested_targets_assigned=sum(len(g.targets) for g in actual),
        seed_object_deliveries=sum(deliveries), seed_objects_per_worker=deliveries,
        seed_delivery_scope='Required seed-object placements per private worker; not bytes or measured network transfers.',
        unit_model=dict(scope='Constructive uniform unit-cost rounds, not wall-clock time or a forecast.',
                        module_slots=workers, seed_rounds=rounds, serial_private_rounds=max(loads),
                        two_stage_rounds=rounds + max(loads)),
        assumptions=['Every seed module is compiled once with compatible dependency provenance before private execution.',
                     'Private components run serially per worker after the entire seed is ready.',
                     'Network, object sizes, memory, task overhead, failures, audits and kernel replay are excluded.'])
    if include_assignments:
        result['seed_module_ids'] = sorted(seed_ids)
        result['assignments'] = [dict(worker=index, groups=[g.task for g in assigned],
            targets=[t for g in assigned for t in g.targets],
            private_module_ids=list(members(private_bits[index], module_ids)))
            for index, assigned in enumerate(assignments)]
    return result
