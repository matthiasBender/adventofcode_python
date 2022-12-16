from typing import Self
import re
from dataclasses import dataclass
from itertools import combinations

@dataclass
class Sensor:
    pos: tuple[int, int]
    beacon: tuple[int, int]
    distance: int

    def in_range(self, x: int, y: int) -> bool:
        dist = abs(x - self.pos[0]) + abs(y - self.pos[1])
        return dist <= self.distance

@dataclass
class Range:
    x1: int
    x2: int

    def overlaps(self, range: Self) -> bool:
        return range.x1 <= self.x1 <= range.x2 or range.x1 <= self.x2 <= range.x2 or self.x1 <= range.x1 <= self.x2

    def __contains__(self, range: Self) -> bool:
        return self.x1 <= range.x1 and range.x2 <= self.x2

    def merge(self, range: Self) -> Self:
        return Range(
            min(self.x1, range.x1),
            max(self.x2, range.x2)
        )

    def __hash__(self) -> int:
        return hash((self.x1, self.x2))

    def get_size(self) -> int:
        return abs(self.x2 - self.x1)


def read_input() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    with open("day15.dat") as f:
        sensors = []
        for line in f.readlines():
            groups = re.search(pattern, line).groups()
            tup = (
                (int(groups[0]), int(groups[1])),
                (int(groups[2]), int(groups[3]))
            )
            sensors.append(Sensor(
                tup[0],
                tup[1],
                abs(tup[0][0] - tup[1][0]) + abs(tup[0][1] - tup[1][1])
            ))
        return sensors

sensors = read_input()


def merge_ranges(ranges: list[Range]) -> list[Range]:
    current = ranges[0]
    remaining = ranges[1:]
    result = []
    for rem in remaining:
        if current.overlaps(rem):
            current = current.merge(rem)
        else:
            result.append(rem)
    if len(remaining) == len(result):
        return ranges
    else:
        result.append(current)
        return merge_ranges(result)


def find_occupied_ranges(sensors: list[Sensor], y_pos: int) -> int:
    ranges: list[Range] = []
    for sensor in sensors:
        y_dist = abs(sensor.pos[1] - y_pos)
        if y_dist <= sensor.distance:
            left_range = sensor.distance - y_dist
            ranges.append(Range(
                sensor.pos[0] - left_range, sensor.pos[0] + left_range
            ))
    return merge_ranges(ranges)


def find_beacon_pos(sensors: list[Sensor], y_range: int) -> int:
    result_ranges = None
    result_y = -1
    for y_pos in range(y_range + 1):
        ranges = find_occupied_ranges(sensors, y_pos)
        if len(ranges) > 1:
            result_ranges = ranges
            result_y = y_pos
            break
    r1, r2 = result_ranges
    result_x = (r2.x1 + r1.x2) // 2 if r1.x2 < r2.x1 else (r1.x1 + r2.x2) // 2
    return result_x * y_range + result_y


print(
    "Solution 1:",
    sum(
        r.get_size()
        for r in merge_ranges(find_occupied_ranges(sensors, 2_000_000))
    )
)
print("Solution 2:", find_beacon_pos(sensors, 4_000_000))
