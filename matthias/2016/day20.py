from typing import Self
from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    def __contains__(self, key: Self | int) -> bool:
        if isinstance(key, int):
            return self.start <= key <= self.end
        elif isinstance(key, Self):
            return self.start <= key.start and self.end >= key.end
        return False

    def overlaps(self, key: Self) -> bool:
        return (
            self.start <= key.start <= self.end + 1
            or self.start - 1 <= key.end <= self.end
            or (key.start <= self.start and key.end >= self.end)
        )

    def __add__(self, other: Self) -> Self:
        return Range(
            start=min(self.start, other.start),
            end=max(self.end, other.end)
        )


def read_input() -> list[Range]:
    with open("day20.dat") as f:
        result: list[Range] = []
        for line in f.readlines():
            first, second = line.strip().split("-")
            result.append(Range(int(first), int(second)))
        return result


input: list[Range] = read_input()


def find_first_range(value: int, ranges: list[Range]) -> Range | None:
    for range in ranges:
        if value in range:
            return range
    return None


def find_lowest_nonblocking(ranges: list[Range] = input):
    current = Range(-2, -1)
    result = -1
    while current:
        result = current.end + 1
        current = find_first_range(result, ranges)
    return result


print("Solution 1:", find_lowest_nonblocking())


def try_merge_all(range: Range, others: list[Range]) -> list[Range]:
    result = []
    current = range
    for other in others:
        if current.overlaps(other):
            current = current + other
        else:
            result.append(other)
    result.append(current)
    return result


def merge_all(ranges: list[Range] = input) -> list[Range]:
    current = ranges
    for range in ranges:
        current = try_merge_all(range, current)
    return current


merged = sorted(merge_all(), key=lambda x: x.start)
print("Solution 2:", sum(
    r2.start - r1.end - 1 for r1, r2 in zip(merged, merged[1:])
))
