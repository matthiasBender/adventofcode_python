from dataclasses import dataclass
import re
import numpy as np


@dataclass
class Command:
    cmd: str
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    @staticmethod
    def from_groups(tuple):
        return Command(
            cmd=tuple[0],
            start_x=int(tuple[1]),
            start_y=int(tuple[2]),
            end_x=int(tuple[3]),
            end_y=int(tuple[4])
        )


def read_input():
    pattern = "([\\w\\s]+) (\\d+),(\\d+) through (\\d+),(\\d+)"
    with open("day06.dat") as f:
        return [
            Command.from_groups(
                re.search(pattern, line).groups()
            ) for line in f.readlines()
        ]


def modify_array(array, command):
    part = array[
        command.start_x:command.end_x + 1,
        command.start_y:command.end_y + 1
    ]
    if command.cmd == "turn on":
        part[:, :] = 1
    elif command.cmd == "turn off":
        part[:, :] = 0
    elif command.cmd == "toggle":
        part[:, :] = (part - 1) * -1
    return area


def modify_array2(array, command):
    part = array[
        command.start_x:command.end_x + 1,
        command.start_y:command.end_y + 1
    ]
    if command.cmd == "turn on":
        part[:, :] += 1
    elif command.cmd == "turn off":
        part[:, :] = np.subtract(part, 1, out=part, where=part > 0)
    elif command.cmd == "toggle":
        part[:, :] += 2
    return area


def print_array(array):
    result = ""
    for row in array:
        for element in row:
            if element:
                result += "#"
            else:
                result += "."
        result += "\n"
    print(result)


commands = read_input()
area = np.zeros((1000, 1000), dtype=int)


# modify_array(area, Command("turn on", 0, 0, 999, 999))
# modify_array(area, Command("toggle", 0, 0, 999, 0))
# modify_array(area, Command("turn off", 499, 499, 500, 500))

for command in commands:
    modify_array(area, command)
print("Rätsel 1: ", area.sum())


area = np.zeros((1000, 1000), dtype=int)
for command in commands:
    modify_array2(area, command)
print("Rätsel 2: ", area.sum())
