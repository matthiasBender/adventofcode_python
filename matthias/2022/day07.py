from typing import Self, Iterable
from dataclasses import dataclass, field
from pprint import pprint


class Node:
    def size(self) -> int:
        raise NotImplementedError()


@dataclass
class File:
    name: str
    file_size: int

    def size(self):
        return self.file_size

@dataclass
class Folder:
    name: str
    parent: Self | None = None
    folders: dict[str, Self] = field(default_factory=dict)
    files: list[File] = field(default_factory=list)

    def size(self) -> int:
        return sum(x.size() for x in self.folders.values()) + sum(x.size() for x in self.files)

    def all_folders(self) -> Iterable[Self]:
        yield self
        for folder in self.folders.values():
            for f in folder.all_folders():
                yield f


def parse_ls(cmd: str, current: Folder):
    for output in cmd.split("\n")[1:]:
        type, name = output.split(" ")
        if type == "dir":
            current.folders[name] = Folder(name, parent=current)
        else:
            current.files.append(File(name, int(type)))


def read_input():
    with open("day07.dat") as f:
        root = Folder("/")
        root.parent = root
        commands = [line.strip() for line in f.read().split("$ ")[1:]]
        current = root
        for command in commands:
            if command == "cd /":
                current = root
            elif command == "cd ..":
                current = current.parent
            elif command.startswith("cd "):
                current = current.folders[command[3:]]
            elif command.startswith("ls"):
                parse_ls(command, current)
        return root


root = read_input()
sizes = sorted([f.size() for f in root.all_folders()])
print("Solution 1:", sum(s for s in sizes if s <= 100_000))

amount_to_free = 30000000 - (70000000 - root.size())
for s in sizes:
    if s >= amount_to_free:
        print("Solution 2:", s)
        break

