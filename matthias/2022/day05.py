import re
import numpy as np
from collections import deque
from dataclasses import dataclass

@dataclass
class Move:
    number: int
    src: int
    to: int

    def __repr__(self) -> str:
        return f"move {self.number} from {self.src} to {self.to}"

    def apply(self, stacks: list[deque[str]]):
        for _ in range(self.number):
            stacks[self.to - 1].append(stacks[self.src - 1].pop())

    def apply_better(self, stacks: list[deque[str]]):
        stacks[self.to - 1].extend(
            [stacks[self.src - 1].pop() for _ in range(self.number)][::-1]
        )

def read_input() -> tuple[list[deque[str]], list[Move]]:
    pattern = r"move (\d+) from (\d) to (\d)"
    with open("day05a.dat") as f1, open("day05b.dat") as f2:
        stack_array = [
            deque([x for x in s if x != " "]) for s in np.array([
                list(line.strip("\n")) for line in f1.readlines()[:-1]
            ])[::-1,1::4].T
        ]
        commands = []
        for line in f2.readlines():
            n, src, to = re.search(pattern, line).groups()
            commands.append(
                Move(int(n), int(src), int(to))
            )
        return stack_array, commands


stacks, commands = read_input()


def apply_all(commands: list[Move] = commands, stacks: list[deque[str]] = stacks, apply_func = Move.apply) -> str:
    for cmd in commands:
        apply_func(cmd, stacks)
    return "".join(s[-1] for s in stacks)

print("Solution 1:", apply_all())
stacks, commands = read_input()
print("Solution 2:", apply_all(commands, stacks, apply_func=Move.apply_better))
