from functools import reduce

ord_a = ord("a")
ord_A = ord("A")


def read_input() -> list[str]:
    with open("day03.dat") as f:
        return [x.strip() for x in f.readlines()]


input = read_input()


def priority(c: str) -> int:
    o = ord(c)
    if o >= ord_a:
        return o - ord_a + 1
    elif o < ord_a:
        return o - ord_A + 27


def find_duplicate_items(rucksack: str) -> set[str]:
    half = len(rucksack) // 2
    return set(rucksack[:half]).intersection(rucksack[half:])


print("Solution 1:", sum(priority(x) for r in input for x in find_duplicate_items(r)))


def find_badge(*strings: list[str]) -> set[str]:
    return reduce(set.intersection, (set(x) for x in strings))


def sum_badges(input: list[str] = input) -> int:
    result = 0
    for i in range(0, len(input), 3):
        result += sum(priority(c) for c in find_badge(*input[i:i + 3]))
    return result


print("Solution 2:", sum_badges())