from hashlib import md5
from multiprocessing import Pool

input = "yzbqklnj"


def find_leading_5zeros(input):
    target_prefix = "00000"
    for i in range(1, 1000000):
        hash = md5((input + str(i)).encode())
        hex = hash.hexdigest()[:5]
        if hex == target_prefix:
            return i
    raise ValueError(f"Could not find it for input {input}!")

print("Rätsel 1: ", find_leading_5zeros(input))

def find_leading_6zeros(input, start_range, end_range):
    target_prefix = "000000"
    start = input.encode()
    for i in range(start_range, end_range):
        hash = md5(start + str(i).encode())
        hex = hash.hexdigest()[:6]
        if hex == target_prefix:
            return i
    return -1

def search_shard(i):
    return find_leading_6zeros(input, i * 1000000 + 1, (i + 1) * 1000000)

with Pool(10) as p:
    print("Rätsel 2: ", [r for r in p.map(search_shard, list(range(10))) if r > -1][0])
