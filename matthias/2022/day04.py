def read_input() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    with open("day04.dat") as f:
        result = []
        for line in f.readlines():
            first, second = line.strip().split(",")
            result.append((
                tuple(int(x) for x in first.split("-")), 
                tuple(int(x) for x in second.split("-"))
            ))
        return result


def is_inside(inner: tuple[int, int], outer: tuple[int, int]) -> bool:
    return outer[0] <= inner[0] and outer[1] >= inner[1]


input = read_input()
print(
    "Solution 1:", 
    sum(is_inside(first, second) or is_inside(second, first) for first, second in input)
)


def overlaps(first: tuple[int, int], second: tuple[int, int]) -> bool:
    return is_inside(first, second) or is_inside(second, first) \
        or second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1]


print("Solution 2:", sum(overlaps(*pair) for pair in input))