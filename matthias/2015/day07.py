from __future__ import annotations
from typing import List, Union, Mapping
import re
from dataclasses import dataclass
from pprint import pprint


MAX_INT = 0xFFFF


@dataclass
class Operation:
    name: str
    inputs: List[Union[str, int]]

    def eval_to_const(self) -> Union[int, Operation]:
        if all(isinstance(i, int) for i in self.inputs):
            if self.name == "NOT":
                return self.inputs[0] ^ MAX_INT # cannot use ~ since it would produce signed results that are not uint16
            elif self.name == "AND":
                return self.inputs[0] & self.inputs[1]
            elif self.name == "OR":
                return self.inputs[0] | self.inputs[1]
            elif self.name == "RSHIFT":
                return self.inputs[0] >> self.inputs[1]
            elif self.name == "LSHIFT":
                return (self.inputs[0] << self.inputs[1]) & MAX_INT # ensure it does not become larger than 16bit
        return self

    def update_inputs(self, wires: Mapping[str, Union[str, int, Operation]]):
        def replace(input: Union[str, int], wires: Mapping[str, Union[str, int, Operation]]) -> Union[str, int]:
            value = wires.get(input, input)
            return value if isinstance(value, int) else input

        self.inputs = [replace(input, wires) for input in self.inputs]


def parse_single(str: str) -> Union[str, int]:
    try:
        return int(str)
    except ValueError:
        return str


def parse_action(str: str) -> Union[str, int, Operation]:
    tokens = str.split(" ")
    if len(tokens) == 1:
        return parse_single(str)
    elif len(tokens) == 2 and tokens[0] == "NOT":
        return Operation("NOT", [parse_single(tokens[1])])
    elif tokens[1] == "AND":
        return Operation("AND", [parse_single(tokens[0]), parse_single(tokens[2])])
    elif tokens[1] == "OR":
        return Operation("OR", [parse_single(tokens[0]), parse_single(tokens[2])])
    elif tokens[1] == "LSHIFT":
        return Operation("LSHIFT", [parse_single(tokens[0]), parse_single(tokens[2])])
    elif tokens[1] == "RSHIFT":
        return Operation("RSHIFT", [parse_single(tokens[0]), parse_single(tokens[2])])
    return str


def read_input() -> Mapping[str, Union[str, int, Operation]]:
    pattern = "([\\w\\s]+) -> (\\w+)"
    with open("day07.dat") as f:
        connections = [
            re.search(pattern, line).groups() for line in f.readlines()
        ]
        return {
            wire: parse_action(action) for (action, wire) in connections
        }


def evaluate(input: Union[str, int, Operation], wires: Mapping[str, Union[str, int, Operation]]) -> Union[int, str, Operation]:
    tp = type(input)
    if tp == int:
        return input
    elif tp == Operation:
        input.update_inputs(wires)
        return input.eval_to_const()
    elif tp == str:
        return wires[input]


wires = read_input()
while not isinstance(wires["a"], int):
    wires = {
        wire:evaluate(action, wires) for (wire, action) in wires.items()
    }
result = wires["a"]
print("Rätsel 1: ", result)

wires = read_input()
wires["b"] = result
while not isinstance(wires["a"], int):
    wires = {
        wire:evaluate(action, wires) for (wire, action) in wires.items()
    }
result = wires["a"]
print("Rätsel 2: ", result)
