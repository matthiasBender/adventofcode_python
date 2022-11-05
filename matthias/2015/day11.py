from re import L
from typing import Any
import numpy as np

offset = 97
alpha_size = 26
illegals = set([ord("o"), ord("l"), ord("i")])

input = "hepxcrrq"

def str_to_array(input: str):
    return np.array([
        ord(i) - offset for i in input
    ], dtype = int)

def array_to_str(arr) -> str:
    return "".join(chr(i + offset) for i in arr)


def inc_array(arr):
    arr[-1] = (arr[-1] + 1) % alpha_size
    if arr.size > 1 and arr[-1] == 0:
        inc_array(arr[:-1])


def is_valid(arr) -> bool:
    has_straight = any(
        second == first + 1 and third == second + 1 
        for (first, second, third) in zip(arr, arr[1:], arr[2:])
    )
    # print(has_straight)
    pair_positions = np.where(arr[:-1] == arr[1:])[0]
    has_pair = pair_positions.size >= 2 and pair_positions[-1] - pair_positions[0] >= 2
    # print(has_pair)
    has_no_illegal = all(i not in illegals for i in arr)
    # print(has_no_illegal)
    return has_straight and has_pair and has_no_illegal


result = str_to_array(input)
while not is_valid(result):
    inc_array(result)

print("Rätsel 1: ", array_to_str(result))

inc_array(result)
while not is_valid(result):
    inc_array(result)

print("Rätsel 2: ", array_to_str(result))

