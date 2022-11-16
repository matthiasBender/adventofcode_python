import re
from random import shuffle

medicine = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"


def read_input():
    pattern = "(\\w+) => (\\w+)"
    with open("day19.dat") as f:
        return [re.search(pattern, line).groups() for line in f.readlines()]

replacements = read_input()


def generate_all_molecules(start, replacement):
    parts = start.split(replacement[0])
    results = []
    for i in range(len(parts) - 1):
        results.append(
            replacement[0].join(parts[:i + 1]) + replacement[1] + replacement[0].join(parts[i + 1:])
        )
    return results


def find_all_possible(molecule, replacements):
    return set(x for repl in replacements for x in generate_all_molecules(molecule, repl))

print("Rätsel 1:", len(find_all_possible(medicine, replacements)))


def count_repl_steps(start="e", target=medicine, replacements=replacements):
    steps = 0
    t = target
    
    while t != start:
        tmp = t
        for first, second in replacements:
            if second not in t:
                continue
            t = t.replace(second, first, 1)
            steps +=1

        if tmp == t:
            t = target
            steps = 0
            shuffle(replacements)
    return steps
    


print("Rätsel 2:", count_repl_steps())
