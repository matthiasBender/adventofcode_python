from intcode import *

input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0"


def execute_task(code: list[int], noun: int = 12, verb: int = 2) -> int:
    exec = Execution(code.copy())
    exec.program[1] = noun
    exec.program[2] = verb
    exec.run_program()
    return exec.program[0]


code = read_int_code(input)
print("Solution 1:", execute_task(code))


def find_output_19690720(code: list[int]) -> int:
    for noun in range(100):
        for verb in range(100):
            if execute_task(code, noun, verb) == 19690720:
                return 100 * noun + verb


print("Solution 2:", find_output_19690720(code))
