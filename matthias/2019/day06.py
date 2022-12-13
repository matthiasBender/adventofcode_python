from collections import defaultdict, deque


def read_input():
    with open("day06.dat") as f:
        return [tuple(line.strip().split(")")) for line in f.readlines()]

def count_orbits(orbits: dict[str, list[str]], start: str = "COM", depth: int = 0) -> int:
    children = orbits.get(start, [])
    return depth + sum(count_orbits(orbits, child, depth + 1) for child in children)


def find_shortest_path(
    orbits: dict[str, list[str]],
    reverse_orbits: dict[str, list[str]],
    start: str = "YOU", target: str = "SAN"
) -> int:
    q = deque([(start, 0)])
    known = set([start])
    while q:
        current, depth = q.popleft()
        if current == target:
            return depth - 2
        depth += 1
        next_nodes = orbits.get(current, []) + reverse_orbits.get(current, [])
        q.extend(
            (next, depth)
            for next in next_nodes
            if next not in known
        )
        known = known.union(next_nodes)
    print("NOT FOUND!!!")



orbits = defaultdict(list)
for key, value in read_input():
    orbits[key].append(value)
reverse_orbits = defaultdict(list)
for key, value in read_input():
    reverse_orbits[value].append(key)
print("Solution 1:", count_orbits(orbits))
print("Solution 2:", find_shortest_path(orbits, reverse_orbits))