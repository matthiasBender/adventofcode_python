from typing import Any, Iterable
from gmpy2 import popcount
from collections import deque


input = 1352


def is_no_wall(x: int, y: int, input: int = input) -> bool:
    s = (x + y)
    num = s * s + 3 * x + y + input
    return popcount(num) % 2 == 0


def get_neighborhood(pos: tuple[int, int]) -> Iterable[tuple[int, int]]:
    x, y = pos
    if x > 0:
        yield (x - 1, y)
    if y > 0:
        yield (x, y - 1)
    yield (x + 1, y)
    yield (x, y + 1)


def expand(pos: tuple[int, int], seen: dict[tuple[int, int], Any]) -> Iterable[tuple[int, int]]:
    for p in get_neighborhood(pos):
        if p not in seen and is_no_wall(p[0], p[1]):
            yield p


def find_route(target: tuple[int, int] = (31, 39), start: tuple[int, int] = (1, 1)) -> tuple[int, dict[tuple[int, int], int]]:
    seen = {start: 0}
    to_visit = deque([start])
    while to_visit:
        pos = to_visit.popleft()
        step = seen[pos]
        if pos == target:
            return step, seen
        for p in expand(pos, seen):
            to_visit.append(p)
            seen[p] = step + 1


result, seen = find_route()
print("Solution 1:", result)

ranges = sum(1 for _, steps in seen.items() if steps <= 50)
print("Solution 2:", ranges)
