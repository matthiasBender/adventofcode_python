from typing import List

def read_input() -> List[str]:
    with open("day08.dat") as f:
        return [l.strip() for l in f.readlines()]


lines = read_input()
sizes = sum(len(l) for l in lines)

def unescape(s: str) -> str:
    unquoted = s[1:-1]
    result = ""
    last = ""
    for c in unquoted:
        esc_seq = last + c
        if esc_seq == '\\"':
            result += c
            last = ""
        elif esc_seq == '\\\\':
            result += c
            last = ""
        elif esc_seq.startswith('\\x') and len(esc_seq) < 4:
            last = esc_seq
        elif esc_seq.startswith('\\x') and len(esc_seq) == 4:
            result += chr(int("0x" + esc_seq[2:], 0))
            last = ""
        elif c == '\\':
            last = c
        else:
            result += c
            last = ""
    return result

unescaped_sizes = sum(len(unescape(l)) for l in lines)
print("Rätsel 1: ", sizes - unescaped_sizes)

def escape(s: str) -> str:
    result = '"'
    for c in s:
        if c == '"' or c == '\\':
            result += '\\'
        result += c
    return result + '"'

escaped_sizes = sum(len(escape(l)) for l in lines)
print("Rätsel 2: ", escaped_sizes - sizes)