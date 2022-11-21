import re
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Room:
    name: str
    sector_id: int
    checksum: str

    def is_valid(self) -> bool:
        counts = defaultdict(int)
        for c in self.name:
            counts[c] += 1
        checksum = "".join(sorted(
            counts.keys(),
            key=lambda x: (counts[x], 1 / ord(x)),
            reverse=True
        )[:5])
        return checksum == self.checksum

    def decrypt(self) -> str:
        return "".join([
            chr(((ord(c) - 97) + self.sector_id) % 26 + 97)
            for c in self.name
        ])


def read_input() -> list[Room]:
    pattern = "([-\\w]+)-(\\d+)\\[(\\w+)\\]"
    with open("day04.dat") as f:
        rooms = []
        for line in f.readlines():
            (name, sector_id, checksum) = re.search(pattern, line).groups()
            rooms.append(Room(name.replace("-", ""), int(sector_id), checksum))
        return rooms


rooms = read_input()

print("Puzzle 1:", sum(room.sector_id for room in rooms if room.is_valid()))

for room in rooms:
    if room.decrypt() == "northpoleobjectstorage":
        print("Puzzle 2:", room.sector_id)
