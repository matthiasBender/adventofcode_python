import numpy as np


def read_input() -> list[str]:
    with open("day02.dat") as f:
        return [line.strip() for line in f.readlines()]


input = read_input()
grid = np.arange(9, dtype=int).reshape((3, 3)) + 1


def get_digit(s: str, grid) -> int | str:
    pos = np.ones(2, dtype=int)

    for c in s:
        if c == "U" and pos[0] > 0 and grid[pos[0] - 1, pos[1]] != '#':
            pos[0] -= 1
        elif c == "D" and pos[0] < grid.shape[0] - 1 and grid[pos[0] + 1, pos[1]] != '#':
            pos[0] += 1
        elif c == "R" and pos[1] < grid.shape[1] - 1 and grid[pos[0], pos[1] + 1] != '#':
            pos[1] += 1
        elif c == "L" and pos[1] > 0 and grid[pos[0], pos[1] - 1] != '#':
            pos[1] -= 1
    return grid[tuple(pos)]


def calculate_number(input: list[str], grid) -> str:
    return "".join(
        str(get_digit(ll, grid)) for ll in input
    )


print("Puzzle 1:", calculate_number(input, grid))
grid = np.array([
    ['#', '#', '1', '#', '#'],
    ['#', '2', '3', '4', '#'],
    ['5', '6', '7', '8', '9'],
    ['#', 'A', 'B', 'C', '#'],
    ['#', '#', 'D', '#', '#'],
])
print("Puzzle 2:", calculate_number(input, grid))
