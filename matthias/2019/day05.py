from intcode import *

program = open("day05.dat").read().strip()

def run_diagnostic(code: list[int], diagnostic: int=1) -> int:
    result = []
    exec = Execution(
        code.copy(),
        input_func=lambda: print(f"providing diagnostic for {diagnostic}") or diagnostic,
        output_func=result.append
    )
    exec.run_program()
    return result


code = read_int_code(program)
print("Solution 1:", run_diagnostic(code)[-1])
print("Solution 2:", run_diagnostic(code, 5)[0])
