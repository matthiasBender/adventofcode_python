import numpy.typing as npt
import numpy as np

input = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"


def parse_input(input: str = input) -> list[tuple[str, int]]:
    return [(x[0], int(x[1:])) for x in input.split(", ")]


def calculate_distance(path: list[tuple[str, int]]) -> int:
    horizontal, vertical = 0, 0
    h_correct = 1
    v_correct = 1
    for (index, (direction, distance)) in enumerate(path):
        if index % 2 == 0:
            if direction == "R":
                horizontal += distance * h_correct
                v_correct *= -1
            else:
                horizontal -= distance * h_correct
                h_correct *= -1
        else:
            if direction == "R":
                vertical += distance * v_correct
                h_correct *= -1
            else:
                vertical -= distance * v_correct
                v_correct *= -1
    return abs(horizontal) + abs(vertical)


path = parse_input()
print("Puzzle 1:", calculate_distance(path))


def followup_direction(old, new: str):
    if np.array_equal(old, np.array([1, 0])):
        return np.array([0, -1]) if new == "R" else np.array([0, 1])
    elif np.array_equal(old, np.array([0, 1])):
        return np.array([1, 0]) if new == "R" else np.array([-1, 0])
    elif np.array_equal(old, np.array([-1, 0])):
        return np.array([0, 1]) if new == "R" else np.array([0, -1])
    elif np.array_equal(old, np.array([0, -1])):
        return np.array([-1, 0]) if new == "R" else np.array([1, 0])


def find_first_crossing(path: list[tuple[str, int]]) -> int:
    locations: set[tuple[int, int]] = set([(0, 0)])
    position = np.zeros(2, dtype=int)
    last_dir = np.array([1, 0])
    for (direction, distance) in path:
        d = 1 if direction == "R" else -1
        new_locations = [
            position + last_dir * d * (x + 1) for x in range(distance)
        ]
        for nl in new_locations:
            nlt = tuple(nl)
            if nlt in locations:
                return np.abs(nl).sum()
            locations.add(nlt)
        position = new_locations[-1]
        last_dir = followup_direction(last_dir, direction)
    raise ValueError("Could not find duplicate!")


print("Puzzle 2:", find_first_crossing(path))
