from dataclasses import dataclass


@dataclass
class Execution:
    program: list[int]
    program_counter: int = 0

    def execute_opcode(self) -> str | None:
        pc = self.program_counter
        prog = self.program
        opcode = prog[pc]
        match opcode:
            case 1:  # add arguments
                arg1 = prog[pc + 1]
                arg2 = prog[pc + 2]
                result = prog[pc + 3]
                prog[result] = prog[arg1] + prog[arg2]
                self.program_counter += 4
            case 2:  # multiply arguments
                arg1 = prog[pc + 1]
                arg2 = prog[pc + 2]
                result = prog[pc + 3]
                prog[result] = prog[arg1] * prog[arg2]
                self.program_counter += 4
            case 99:  # halt program
                return "halt"

    def run_program(self):
        result = ""
        while result != "halt":
            result = self.execute_opcode()


def read_int_code(s: str) -> list[int]:
    return [int(x) for x in s.split(",")]
