def read_input() -> list[int]:
    with open("day01.dat") as f:
        return [int(line.strip()) for line in f.readlines()]


def calculate_fuel(x: int) -> int:
    return x // 3 - 2


def converge_fuel(x: int) -> int:
    if x == 0:
        return 0
    else:
        return x + converge_fuel(calculate_fuel(x))


input = read_input()
print("Solution 1:", sum(calculate_fuel(x) for x in input))
print("Solution 2:", sum(calculate_fuel(x) + converge_fuel(x) for x in input))

