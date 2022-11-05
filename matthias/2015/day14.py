from typing import List
import re
from dataclasses import dataclass
from xmlrpc.client import boolean


@dataclass
class Reindeer:
    name: str
    speed: int
    fly_time: int
    rest_time: int


@dataclass
class Run:
    deer: Reindeer
    position: int
    resting: boolean
    timer: int

    def move(self):
        self.timer -= 1
        if not self.resting:
            self.position += self.deer.speed
        if self.timer <= 0:
            self.resting = not self.resting
            self.timer = self.deer.rest_time if self.resting else self.deer.fly_time


def read_input() -> List[Reindeer]:
    pattern = "(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    with open("day14.dat") as f:
        tups = [
            re.search(pattern, line).groups() for line in f.readlines()
        ]
        return [
            Reindeer(name, int(speed), int(fly_time), int(rest_time)) 
            for (name, speed, fly_time, rest_time) in tups
        ]


def simulate_steps(deers: List[Reindeer], number_of_steps=2503):
    runs = [
        Run(deer, 0, False, deer.fly_time) for deer in deers
    ]
    for step in range(number_of_steps):
        for run in runs:
            run.move()

    return max(r.position for r in runs)

deers = read_input()

print("Rätsel 1:", simulate_steps(deers))

def simulate_scored(deers: List[Reindeer], number_of_steps=2503):
    runs = [
        Run(deer, 0, False, deer.fly_time) for deer in deers
    ]
    scores = { deer.name: 0 for deer in deers }
    for step in range(number_of_steps):
        fastest = []
        lead_pos = 0
        for run in runs:
            run.move()
            if run.position > lead_pos:
                lead_pos = run.position
                fastest = [run.deer.name]
            elif run.position == lead_pos:
                fastest.append(run.deer.name)
        for deer in fastest:
            scores[deer] += 1

    return max(scores.values())

print("Rätsel 2:", simulate_scored(deers))
