from typing import Self, Any
from dataclasses import dataclass
import numpy as np
import numpy.typing as npt
from itertools import combinations
from collections import deque


@dataclass
class State:
    elevator: int
    generators: npt.NDArray[np.int8]
    micros: npt.NDArray[np.int8]

    def is_valid(self) -> bool:
        return all(
            np.alltrue(self.generators != e)
            or np.alltrue(
                self.generators[np.where(self.micros == e)[0]] == e
            )
            for e in range(self.elevator - 1, self.elevator + 2)
        )

    def is_done(self) -> bool:
        return np.alltrue(self.generators == 4) and np.alltrue(self.micros == 4)

    def copy(self) -> Self:
        return State(self.elevator, np.copy(self.generators), np.copy(self.micros))

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, self.__class__)
            and self.elevator == other.elevator
            and sorted(zip(self.generators, self.micros)) == sorted(zip(other.generators, other.micros))
        )

    def __hash__(self) -> int:
        return self.elevator + hash(tuple(sorted(zip(self.generators, self.micros))))


input = np.array([
    [1, 1],  # promethium
    [3, 2],  # cobalt
    [3, 2],  # curium
    [3, 2],  # ruthenium
    [3, 2],  # plutonium
], dtype=np.int8)
input2 = np.array([
    [1, 1],  # promethium
    [3, 2],  # cobalt
    [3, 2],  # curium
    [3, 2],  # ruthenium
    [3, 2],  # plutonium
    [1, 1],  # elerium
    [1, 1],  # dilithium
], dtype=np.int8)

initial_state = State(1, input[:, 1], input[:, 0])
initial_state2 = State(1, input2[:, 1], input2[:, 0])


def move_elevator(state: State, elevator: int, gens: list[int], mics: list[int]) -> State:
    result = state.copy()
    result.elevator = elevator
    result.generators[gens] = elevator
    result.micros[mics] = elevator
    return result


def generate_pairs(gens: list[int], mics: list[int]) -> list[tuple[list[int], list[int]]]:
    possible_items = [None] + [
        (True, i) for i in gens
    ] + [(False, i) for i in mics]
    for x, (type_y, y) in combinations(possible_items, 2):
        gens = []
        mics = []
        if type_y:
            gens.append(y)
        else:
            mics.append(y)
        if x:
            if x[0]:
                gens.append(x[1])
            else:
                mics.append(x[1])
        yield (gens, mics)


def filter_and_register_states(states: list[State], seen: dict[State, Any], depth: int) -> list[State]:
    for state in states:
        if state not in seen:
            seen[state] = depth
            if state.is_valid():
                yield state


def find_next_states(state: State, seen: dict[State, Any]) -> list[State]:
    elevators: list[int] = []
    if state.elevator > 1:
        elevators.append(state.elevator - 1)
    if state.elevator < 4:
        elevators.append(state.elevator + 1)
    available_gens = np.where(state.generators == state.elevator)[0]
    available_mics = np.where(state.micros == state.elevator)[0]
    results: list[State] = [
        move_elevator(state, ele, gs, ms)
        for gs, ms in generate_pairs(available_gens, available_mics)
        for ele in elevators
    ]
    return filter_and_register_states(results, seen, seen[state] + 1)


def find_fastest_way(initial: State) -> int:
    seen = {initial: 0}
    states_for_check = deque([initial])
    while states_for_check:
        state = states_for_check.popleft()
        for s in find_next_states(state, seen):
            if s.is_done():
                return seen[s]
            states_for_check.append(s)


print("Solution 1:", find_fastest_way(initial_state))
print("Solution 2:", find_fastest_way(initial_state2))
