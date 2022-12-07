import re
import numpy as np
from itertools import permutations


def read_input() -> list[tuple[str, int] | tuple[str, int, int] | tuple[str, str, str] | tuple[str, str]]:
    move_pattern = r"move position (\d+) to position (\d+)"
    reverse_pattern = r"reverse positions (\d+) through (\d+)"
    swap_pos_pattern = r"swap position (\d+) with position (\d+)"
    swap_letter_pattern = r"swap letter (\w) with letter (\w)"
    rotate_left_pattern = r"rotate left (\d+) steps*"
    rotate_right_pattern = r"rotate right (\d+) steps*"
    rotate_letter_pattern = r"rotate based on position of letter (\w)"
    with open("day21.dat") as f:
        commands = []
        for line in f.readlines():
            if re.search(move_pattern, line):
                position, target = re.search(move_pattern, line).groups()
                commands.append(("move", int(position), int(target)))
            elif re.search(reverse_pattern, line):
                start, end = re.search(reverse_pattern, line).groups()
                commands.append(("reverse", int(start), int(end)))
            elif re.search(swap_pos_pattern, line):
                pos1, pos2 = re.search(swap_pos_pattern, line).groups()
                commands.append(("swap_pos", int(pos1), int(pos2)))
            elif re.search(swap_letter_pattern, line):
                commands.append(("swap_letter", *re.search(swap_letter_pattern, line).groups()))
            elif re.search(rotate_left_pattern, line):
                commands.append((
                    "rotate_left",
                    int(re.search(rotate_left_pattern, line).groups()[0])
                ))
            elif re.search(rotate_right_pattern, line):
                commands.append((
                    "rotate_right",
                    int(re.search(rotate_right_pattern, line).groups()[0])
                ))
            elif re.search(rotate_letter_pattern, line):
                commands.append((
                    "rotate_letter",
                    re.search(rotate_letter_pattern, line).groups()[0]
                ))
            else:
                print("Failed to parse line: '" + line + "'")
        return commands


message = "abcdefgh"
commands = read_input()


def scramble_single(result, command):
    match command:
        case ("move", pos1, pos2):
            insert = result[pos1:pos1 + 1]
            removed = np.concatenate((result[:pos1], result[pos1 + 1:]))
            result = np.concatenate((removed[:pos2], insert, removed[pos2:]))
            # print("move ", pos1, pos2, "".join(result))
        case ("reverse", start, end):
            result[start:end + 1] = result[start:end + 1][np.arange(end - start, -1, -1)]
            # print("reverse", start, end, "".join(result))
        case ("swap_pos", pos1, pos2):
            result[[pos1, pos2]] = result[[pos2, pos1]]
            # print("swap", pos1, pos2, "".join(result))
        case ("swap_letter", l1, l2):
            for i in range(result.size):
                if result[i] == l1:
                    result[i] = l2
                elif result[i] == l2:
                    result[i] = l1
            # print("swap", l1, l2, "".join(result))
        case ("rotate_left", index):
            result = np.concatenate((result[index:], result[:index]))
            # print("rotate left", index, "".join(result))
        case ("rotate_right", index):
            result = np.concatenate((result[-index:], result[:-index]))
            # print("rotate right", index, "".join(result))
        case ("rotate_letter", l1):
            old = "".join(result)
            index = np.where(result == l1)[0][0] + 1
            rotate = index % result.size if index < 5 else (index + 1) % result.size
            result = np.concatenate((result[-rotate:], result[:-rotate]))
            # print("rotate", l1, index - 1, rotate, "".join(result), f"<- {old}")
    return result


def scramble(message: str, commands: list) -> str:
    result = np.array(list(message))
    for command in commands:
        result = scramble_single(result, command)
    return "".join(result)


print("Solution 1:", scramble(message, commands))


def unscramble(message, commands) -> str:
    for result in permutations(message):
        if scramble(result, commands) == message:
            return "".join(result)


print("Solution 2:", unscramble("fbgdceah", commands))
