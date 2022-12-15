from typing import Iterable

def read_input() -> list[list[tuple[int, int]]]:
    with open("day14.dat") as f:
        result = []
        for line in f.readlines():
            result.append([tuple(int(x) for x in pair.split(",")) for pair in line.strip().split(" -> ")])
        return result


def interpolate_points(start: tuple[int, int], end: tuple[int, int]) -> set[tuple[int, int]]:
    startx, starty = start
    endx, endy = end
    if startx == endx:
        if starty < endy + 1:
            return set([
                (startx, y) for y in range(starty, endy + 1)
            ])
        else:
            return set([
                (startx, y) for y in range(endy, starty + 1)
            ])
    elif starty == endy:
        if startx < endx + 1:
            return set([
                (x, starty) for x in range(startx, endx + 1)
            ])
        else:
            return set([
                (x, starty) for x in range(endx, startx + 1)
            ])
    raise ValueError(f"{start} and {end} are not a straight line!")


def interpolate_path(path: list[tuple[int, int]]) -> set[tuple[int, int]]:
    result = set()
    for p1, p2 in zip(path, path[1:]):
        result = result.union(interpolate_points(p1, p2))
    return result


def interpolate_all(paths: list[list[tuple[int, int]]]) -> set[tuple[int, int]]:
    result = set()
    for path in paths:
        result = result.union(interpolate_path(path))
    return result


def next_position(source: tuple[int, int], occupied: set[tuple[int, int]]) -> tuple[int, int] | None:
    x, y = source
    if (x, y + 1) not in occupied:
        return (x, y + 1)
    if (x - 1, y + 1) not in occupied:
        return (x - 1, y + 1)
    if (x + 1, y + 1) not in occupied:
        return (x + 1, y + 1)
    return None


def drop_single_sand(source: tuple[int, int], occupied: set[tuple[int, int]], max_y: int) -> tuple[int, int] | None:
    if source in occupied:
        return None
    current = source
    next = next_position(source, occupied)
    while next:
        if next[1] > max_y:
            return None
        current = next
        next = next_position(current, occupied)
    return current


def drop_sand(source: tuple[int, int], paths: list[list[tuple[int, int]]], with_floor: bool = False) -> int:
    rocks = interpolate_all(paths)
    max_y = max(y for _, y in rocks)
    if with_floor:
        rocks = rocks.union(interpolate_path(
            [(source[0] - 100 * max_y, max_y + 2), (source[0] + 100 * max_y, max_y + 2)]
        ))
        max_y += 2
    num_occupied = len(rocks)
    last = paths[0][0]
    while last:
        rocks.add(last)
        last = drop_single_sand(source, rocks, max_y)
    return len(rocks) - num_occupied


paths = read_input()
print("Solution 1:", drop_sand((500, 0), paths))
print("Solution 2:", drop_sand((500, 0), paths, with_floor=True))

