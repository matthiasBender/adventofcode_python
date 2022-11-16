from dataclasses import dataclass, field
from typing import List, Union



@dataclass
class Instruction:
    command: str
    arguments: List[Union[str, int]]


@dataclass
class Execution:
    program: List[Instruction]
    reg_a: int = 0
    reg_b: int = 0
    position: int = 0

    def execute_cmd(self):
        instruction = self.program[self.position]
        self.position += 1
        if instruction.command == "hlf":
            self.modify_register(instruction.arguments[0], lambda x: x / 2)
        elif instruction.command == "tpl":
            self.modify_register(instruction.arguments[0], lambda x: x * 3)
        elif instruction.command == "inc":
            self.modify_register(instruction.arguments[0], lambda x: x + 1)
        elif instruction.command == "jmp":
            self.position += instruction.arguments[0] - 1
        elif instruction.command == "jie":
            if self.check_register(instruction.arguments[0]) % 2 == 0:
                self.position += instruction.arguments[1] - 1
        elif instruction.command == "jio":
            if self.check_register(instruction.arguments[0]) == 1:
                self.position += instruction.arguments[1] - 1
    
    def modify_register(self, reg_name: str, f):
        if reg_name == "a":
            self.reg_a = f(self.reg_a)
        elif reg_name == "b":
            self.reg_b = f(self.reg_b)
        else:
            raise Exception("Failed to identify register: " + str(reg_name))

    def check_register(self, reg_name) -> int:
        if reg_name == "a":
            return self.reg_a
        elif reg_name == "b":
            return self.reg_b
        else:
            raise Exception("Failed to identify register: " + str(reg_name))

    def run(self):
        size = len(self.program)
        while self.position < size:
            self.execute_cmd()

def to_int(s: str) -> Union[str, int]:
    try:
        return int(s)
    except:
        return s


def read_input() -> List[Instruction]:
    with open("day23.dat") as f:
        result = []
        for line in f.readlines():
            cmd = line[:3]
            arguments = line[4:].strip().split(", ")
            result.append(Instruction(cmd, [to_int(arg) for arg in arguments]))
        return result


simulation = Execution(read_input())
simulation.run()
print("Rätsel 1:", simulation.reg_b)

simulation = Execution(read_input(), reg_a=1)
simulation.run()
print("Rätsel 2:", simulation.reg_b)
