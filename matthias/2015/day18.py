from dataclasses import dataclass
import numpy as np


@dataclass
class Field:
    board: np.ndarray

    def neighbors(self, x, y):
        shape = self.board.shape
        minX = x - 1 if x > 0 else 0
        minY = y - 1 if y > 0 else 0
        maxX = x + 2 if x < shape[0] - 1 else x + 1
        maxY = y + 2 if y < shape[1] - 1 else y + 1
        return self.board[x, y], self.board[minX:maxX, minY:maxY]

    def calculate_light(self, light, neighbors):
        s = neighbors.sum()
        if s == 3:
            return 1
        if light and s == 4:
           return 1
        return 0 

    def step(self, light_corners=False):
        shape = self.board.shape
        new_board = self.board.copy()

        for x in range(shape[0]):
            for y in range(shape[1]):
                new_board[x, y] = self.calculate_light(*self.neighbors(x, y))
        self.board = new_board
        if light_corners:
            self.board[0, 0] = 1
            self.board[0, shape[1] - 1] = 1
            self.board[shape[0] - 1, 0] = 1
            self.board[shape[0] - 1, shape[1] - 1] = 1

    def __repr__(self) -> str:
        return "\n".join(["".join(["#" if f else "." for f in row]) for row in self.board])

def read_input():
    with open("day18.dat") as f:
        return Field(np.array([
            [0 if c == "." else 1 for c in line.strip()]
            for line in f.readlines()
        ]))


field = read_input()
for i in range(100):
    field.step()

print("Rätsel 1:", field.board.sum())

field = read_input()
field.board[0, 0] = 1
field.board[0, 99] = 1
field.board[99, 0] = 1
field.board[99, 99] = 1
for i in range(100):
    field.step(light_corners=True)

print("Rätsel 2:", field.board.sum())
