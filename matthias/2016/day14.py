from dataclasses import dataclass
from hashlib import md5
from collections import deque

input = "qzyelonm"


@dataclass
class Hash:
    number: int
    hash: str
    triple: str
    quintuples: list[str]


def hash_md5(input: str = input, number: int = 0, stretching: int = 0) -> Hash:
    hash = md5((input + str(number)).encode()).hexdigest()
    for i in range(stretching):
        hash = md5(hash.encode()).hexdigest()
    triple = None
    quintuples = []
    for c1, c2, c3, c4, c5 in zip(hash, hash[1:], hash[2:], hash[3:], hash[4:]):
        if c3 == c4 == c5 or c1 == c2 == c3:
            triple = c3 if not triple else triple
            if c2 == c4 and c1 == c5:
                quintuples.append(c3)
    return Hash(number, hash, triple, quintuples)


def queue_hashes(prefix: str, start: int, end: int, queue: deque[Hash], stretching: int):
    for i in range(start, end):
        hash = hash_md5(prefix, i, stretching=stretching)
        if hash.triple:
            queue.append(hash)


def search_keys(start_value: str = input, stretching: int = 0):
    hashes: deque[Hash] = deque()
    queue_hashes(start_value, 0, 1001, hashes, stretching)
    current = 0
    result_keys = []
    while hashes:
        hash = hashes.popleft()
        queue_hashes(start_value, current + 1001, 1001 + hash.number, hashes, stretching)
        current = hash.number
        if any(hash.triple in h.quintuples for h in hashes):
            result_keys.append(hash)
            if len(result_keys) >= 64:
                return result_keys[-1]


print("Solution 1:", search_keys().number)

print("Solution 2:", search_keys(stretching=2016).number)
