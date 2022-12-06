from typing import Self
import numpy as np
from collections import deque
from dataclasses import dataclass


input = 3_014_603


def find_remaining_elf(num_elves: int = input) -> int:
    total_elves = np.arange(num_elves, dtype=np.int32) + 1
    starting_index = 0
    while total_elves.size > 1:
        next_index = (starting_index + total_elves.size) % 2
        total_elves = total_elves[starting_index::2]
        starting_index = next_index
    return total_elves[0]


def find_remaining_elf_fast(num_elves: int = input) -> int:
    """
    The josephus problem solved the optimal way as described in https://www.youtube.com/watch?v=uCsD3ZGzMgE.
    """
    return int(bin(num_elves)[3:] + "1", 2)


print("Solution 1:", find_remaining_elf())
print("Solution 1 (optimal):", find_remaining_elf_fast())


@dataclass
class Node:
    value: int
    next: Self = None
    prev: Self = None

    def delete_and_next(self) -> Self | None:
        next = self.next
        if self.prev:
            self.prev.next = next
        if next:
            next.prev = self.prev
        return next

    def __repr__(self) -> str:
        result = ""
        if self.prev:
            result += f"{self.prev.value} - "
        result += f"<{self.value}>"
        if self.next:
            result += f" - {self.next.value}"
        return result


def create_linked_list(lst: list[int]) -> Node | None:
    if len(lst) == 0:
        return None
    start = Node(lst[0])
    prev = start
    for item in lst[1:]:
        current = Node(item, prev=prev)
        prev.next = current
        prev = current
    start.prev = current
    current.next = start
    return start


def steal_across(num_elves: int = input) -> int:
    total_elves = [i + 1 for i in range(num_elves)]
    first = create_linked_list(total_elves)
    middle = first
    for _ in range(num_elves // 2):
        middle = middle.next
    rotate_full = num_elves % 2 != 0
    while first.next.value != first.value:
        middle = middle.delete_and_next()
        first = first.next
        if rotate_full:
            middle = middle.next
        rotate_full = not rotate_full
    return first.value


print("Solution 2:", steal_across())
