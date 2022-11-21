from hashlib import md5
from multiprocessing import Pool

input = "abbhdwsy"


def find_leading_5zeros(input: str = input, prefix="00000", start_index=0):
    length = len(prefix)
    for i in range(start_index, 100_000_000):
        hash = md5((input + str(i)).encode())
        hex = hash.hexdigest()[:length]
        if hex == prefix:
            return i, hash.hexdigest()[length:length + 2]
    raise ValueError(f"Could not find it for input {input}!")


def find_password(input: str) -> str:
    start = -1
    result = []
    for i in range(8):
        start, c = find_leading_5zeros(input, start_index=start + 1)
        result.append(c[0])
    return "".join(result)


print("Puzzle 1: ", find_password(input))


def to_int(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        return None


def improved_password(input: str) -> str:
    start = -1
    result = [" ", " ", " ", " ", " ", " ", " ", " "]
    while " " in result:
        start, c = find_leading_5zeros(input, start_index=start + 1)
        n = to_int(c[0])
        if n is not None and n < 8 and result[n] == " ":
            result[n] = c[1]
            print(result)
    return "".join(result)


print(improved_password(input))
