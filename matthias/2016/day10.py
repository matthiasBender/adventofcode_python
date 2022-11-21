import re
from dataclasses import dataclass
from collections import defaultdict
from queue import Queue


@dataclass
class InputInstruction:
    bot: int
    chip: int


@dataclass
class TransferInstruction:
    bot: int
    target_low: int
    target_high: int
    low_is_bot: bool
    high_is_bot: bool


def read_input():
    input_pattern = r'value (\d+) goes to bot (\d+)'
    transfer_pattern = r'bot (\d+) gives low to ((bot)|(output)) (\d+) and high to ((bot)|(output)) (\d+)'
    with open("day10.dat") as f:
        inputs: list[InputInstruction] = []
        transfers: dict[int, TransferInstruction] = {}
        for line in f.readlines():
            match = re.search(transfer_pattern, line)
            if match:
                bot, low_is_bot, _, _, target_low, high_is_bot, _, _, target_high = match.groups()
                transfers[int(bot)] = TransferInstruction(int(bot), int(target_low), int(target_high), low_is_bot == "bot", high_is_bot == "bot")
                continue
            match = re.search(input_pattern, line)
            if match:
                chip, bot = match.groups()
                inputs.append(InputInstruction(int(bot), int(chip)))
        return inputs, transfers


inputs, transfers = read_input()


def transfer_chip(
    outputs: dict[int, list[int]],
    state: dict[int, list[int]],
    chip: int,
    target: int,
    is_bot: bool
) -> None | int:
    if is_bot:
        lst = state[target]
        lst.append(chip)
        if len(lst) > 1:
            return target
    else:
        outputs[target] = chip


def simulate_operation(inputs: list[InputInstruction], transfers: dict[int, TransferInstruction]):
    outputs: dict[int, int] = {}
    double_chips: Queue[int] = Queue()
    state: dict[int, list[int]] = defaultdict(list)
    for input in inputs:
        state[input.bot].append(input.chip)
        if len(state[input.bot]) > 1:
            double_chips.put(input.bot)

    while not double_chips.empty():
        bot = double_chips.get()
        chip1, chip2 = sorted(state[bot])
        instruction = transfers[bot]
        if ((instruction.low_is_bot and len(state[instruction.target_low]) > 1)
                or (instruction.high_is_bot and len(state[instruction.target_high]) > 1)):
            double_chips.put(bot)
            continue
        if chip1 == 17 and chip2 == 61:
            print("Puzzle 1:", bot)
            # break
        split = transfer_chip(outputs, state, chip1, instruction.target_low, instruction.low_is_bot)
        if split or split == 0:
            double_chips.put(split)
        split = transfer_chip(outputs, state, chip2, instruction.target_high, instruction.high_is_bot)
        if split or split == 0:
            double_chips.put(split)
        state[bot] = []  # reset bot before transfering the chips to others.
    return outputs


outputs = simulate_operation(inputs, transfers)
print("Puzzle 2:", outputs[0] * outputs[1] * outputs[2])
