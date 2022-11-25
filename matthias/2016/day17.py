from typing import Self, Any
from dataclasses import dataclass, field
from hashlib import md5
import numpy as np
import numpy.typing as npt
from collections import deque
from queue import PriorityQueue

input = "pxxbnzuo"
target = np.array([3, 3], dtype=np.int8)

movements: tuple[str, npt.NDArray[np.int_], int] = [
    ("U", np.array([0, -1], dtype=np.int8), 0),
    ("D", np.array([0, 1], dtype=np.int8), 1),
    ("L", np.array([-1, 0], dtype=np.int8), 2),
    ("R", np.array([1, 0], dtype=np.int8), 3),
]


@dataclass
class Path:
    input: str = input
    path: str = ""
    position: npt.NDArray[np.int_] = field(default_factory=lambda: np.zeros(2, dtype=np.int8))

    def next(self) -> list[Self]:
        if self.is_target():
            return []
        hash = md5((self.input + self.path).encode()).hexdigest()[:4]
        result: list[Path] = []
        for direction, movement, h_index in movements:
            new_pos = self.position + movement
            if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4 and hash[h_index] > "a":
                result.append(Path(self.input, self.path + direction, new_pos))
        return result

    def is_target(self) -> bool:
        return (self.position - target).sum() == 0


def find_shortest_path(input: str = input) -> Path:
    queue: deque[Path] = deque([Path(input)])
    while queue:
        current = queue.popleft()
        if current.is_target():
            return current
        queue.extend(current.next())


def find_longest_path(input: str = input) -> int:
    queue: deque[Path] = deque([Path(input)])
    path_length = -1
    while queue:
        current = queue.popleft()
        if current.is_target() and len(current.path) > path_length:
            path_length = len(current.path)
        queue.extend(current.next())
    return path_length


print("Solution 1:", find_shortest_path().path)
print("Solution 2:", find_longest_path())
