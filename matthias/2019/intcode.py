from typing import Callable
from dataclasses import dataclass


@dataclass
class Execution:
    """
    Required for the following days and thus might be very generic:
    * day02
    * day05
    """
    program: list[int]
    program_counter: int = 0
    input_func: Callable[[], int] = lambda: int(input("Enter Integer: "))
    output_func: Callable[[int], None] = lambda x: print("Output:", x)

    def execute_opcode(self) -> str | None:
        pc = self.program_counter
        prog = self.program
        opcode = prog[pc] % 100
        arg_modes = prog[pc] // 100
        arg_modes = (arg_modes % 10, arg_modes // 10 % 10, arg_modes // 100 % 10)
        match opcode:
            case 1:  # add arguments
                arg1 = self.read_arg(pc + 1, arg_modes[0])
                arg2 = self.read_arg(pc + 2, arg_modes[1])
                result = prog[pc + 3]
                prog[result] = arg1 + arg2
                self.program_counter += 4
            case 2:  # multiply arguments
                arg1 = self.read_arg(pc + 1, arg_modes[0])
                arg2 = self.read_arg(pc + 2, arg_modes[1])
                result = prog[pc + 3]
                prog[result] = arg1 * arg2
                self.program_counter += 4
            case 3:  # input value
                arg = prog[pc + 1]
                prog[arg] = self.input_func()
                self.program_counter += 2
            case 4:  # output value
                arg = self.read_arg(pc + 1, arg_modes[0])
                self.output_func(arg)
                self.program_counter += 2
            case 5:  # jump-if-true
                arg1 = self.read_arg(pc + 1, arg_modes[0])
                arg2 = self.read_arg(pc + 2, arg_modes[1])
                if arg1:
                    self.program_counter = arg2
                else:
                    self.program_counter += 3
            case 6:  # jump-if-false
                arg1 = self.read_arg(pc + 1, arg_modes[0])
                arg2 = self.read_arg(pc + 2, arg_modes[1])
                if arg1:
                    self.program_counter += 3
                else:
                    self.program_counter = arg2
            case 7:  # less than
                arg1 = self.read_arg(pc + 1, arg_modes[0])
                arg2 = self.read_arg(pc + 2, arg_modes[1])
                result = prog[pc + 3]
                prog[result] = 1 if arg1 < arg2 else 0
                self.program_counter += 4
            case 8:  # equals
                arg1 = self.read_arg(pc + 1, arg_modes[0])
                arg2 = self.read_arg(pc + 2, arg_modes[1])
                result = prog[pc + 3]
                prog[result] = 1 if arg1 == arg2 else 0
                self.program_counter += 4
            case 99:  # halt program
                return "halt"
            case any:
                raise ValueError(f"OpCode {any} is not supported! arg_modes={arg_modes}, pc={pc}")

    def read_arg(self, pc: int, arg_mode: int) -> int:
        source = self.program[pc]
        match arg_mode:
            case 0:
                return self.program[source]
            case 1:
                return source
        raise ValueError(f"arg_mode={arg_mode} is not supported!")

    def run_program(self):
        result = ""
        while result != "halt":
            result = self.execute_opcode()


def read_int_code(s: str) -> list[int]:
    return [int(x) for x in s.split(",")]
