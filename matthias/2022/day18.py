from typing import Iterable
import numpy as np
from collections import deque

def read_input():
    return np.loadtxt("day18.dat", delimiter=",", dtype=np.int64)


def bordering_voxels(x: int, y: int, z: int) -> Iterable[tuple[int, int, int]]:
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)


def is_surrounded(start: tuple[int, int, int], data: set[tuple[int, int, int]], max_coord: tuple[int, int, int]) -> bool:
    q = deque([start])
    found = set([start])
    while q:
        x, y, z = q.popleft()
        if x > max_coord[0] or y > max_coord[1] or z > max_coord[2] or x < 0 or y < 0 or z < 0:
            return False
        for next in bordering_voxels(x, y, z):
            if next not in data and next not in found:
                q.append(next)
                found.add(next)
    return True


def count_free_sides(voxels: list[tuple[int, int, int]], exclude_inside: bool = False) -> int:
    max_coord = np.max(voxels, axis=0)
    data = set(tuple(v) for v in voxels)
    return sum(
        1 for v in data
        for p in bordering_voxels(*v)
        if p not in data and (not exclude_inside or not is_surrounded(p, data, max_coord))
    )


voxels = read_input()
print("Solution 1:", count_free_sides(voxels))
print("Solution 2:", count_free_sides(voxels, exclude_inside=True))
