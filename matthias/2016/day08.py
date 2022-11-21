import re
import numpy as np
import numpy.typing as npt


def read_input() -> list[tuple[str, int, int]]:
    pattern_rect = r'rect (\d+)x(\d+)'
    pattern_row = r'rotate row y=(\d+) by (\d+)'
    pattern_col = r'rotate column x=(\d+) by (\d+)'
    with open("day08.dat") as f:
        result = []
        for line in f.readlines():
            match = re.search(pattern_rect, line)
            if match:
                result.append(("rect", *[int(x) for x in match.groups()]))
                continue
            match = re.search(pattern_row, line)
            if match:
                result.append(("row", *[int(x) for x in match.groups()]))
                continue
            match = re.search(pattern_col, line)
            if match:
                result.append(("col", *[int(x) for x in match.groups()]))
        return result


def apply_action(screen: npt.NDArray[np.bool_], action: tuple[str, int, int]):
    match action[0]:
        case "rect":
            screen[0:action[2], 0:action[1]] = True
        case "row":
            screen[action[1], :] = np.concatenate((
                screen[action[1], -action[2]:],
                screen[action[1], :-action[2]],
            ))
        case "col":
            screen[:, action[1]] = np.concatenate((
                screen[-action[2]:, action[1]],
                screen[:-action[2], action[1]],
            ))


def run_all(screen: npt.NDArray[np.bool_], actions: list[tuple[str, int, int]]):
    for action in actions:
        apply_action(screen, action)


input = read_input()
screen = np.zeros((6, 50), dtype=bool)
run_all(screen, input)

print("Puzzle 1:", screen.sum())
print("Puzzle2:")


def render(screen: npt.NDArray[np.bool_]):
    result = ""
    for row in screen:
        for c in row:
            result += "#" if c else " "
        result += "\n"
    print(result)


render(screen)
