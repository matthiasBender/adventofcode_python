import numpy as np
import numpy.typing as npt


def read_input() -> npt.NDArray[int]:
    with open("day10.dat") as f:
        result = []
        for line in f.readlines():
            result.append(
                line.strip().split(" ")
            )
        return np.array([
            int(x[1]) if len(x) == 2 else 0
            for x in result
        ])


def calculate_cycles(input: npt.NDArray[int]) -> npt.NDArray[int]:
    cycles = np.ones(input.shape, dtype=np.int64)
    cycles[input != 0] += 1
    return cycles


def find_strength_at_cycle(cycles, signals, target_cycle: int) -> int:
    if target_cycle < cycles[0] + 1:
        return 1
    return signals[cycles <= target_cycle - 1][-1]


def sum_target_signals(input, target_signals: list[int]) -> int:
    strengths = input.cumsum() + 1
    cycles = calculate_cycles(input).cumsum()
    return sum(
        find_strength_at_cycle(cycles, strengths, x) * x
        for x in target_signals
    )


input = read_input()
target_cycles = [20, 60, 100, 140, 180, 220]
print("Solution 1:", sum_target_signals(input, target_cycles))


def render_image(input) -> str:
    strengths = input.cumsum() + 1
    cycles = calculate_cycles(input).cumsum()
    result = ""
    for x in range(240):
        signal = find_strength_at_cycle(cycles, strengths, x + 1)
        line_pos = x % 40
        result += "#" if signal - 1 <= line_pos <= signal + 1 else "."
        if line_pos == 39:
            print(result)
            result = ""

print("Solution 2:")
render_image(input)