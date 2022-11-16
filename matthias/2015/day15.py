import numpy as np
import re


max_content = 100


def read_input():
    pattern = "(\\w+): capacity ([-\\d]+), durability ([-\\d]+), flavor ([-\\d]+), texture ([-\\d]+), calories (\\d+)"
    with open("day15.dat") as f:
        ingredients = [
            re.search(pattern, line).groups() for line in f.readlines()
        ]
        result = np.array([
            [int(cap), int(dur), int(flav), int(text), int(cal)] for (_, cap, dur, flav, text, cal) in ingredients
        ])
        return result


def generate_recipes():
    for x1 in range(101):
        for x2 in range(101 - x1):
            for x3 in range(101 - x1 - x2):
                yield [x1, x2, x3, 100 - x1 - x2 - x3]


ingredients = read_input()
ingredients_no_cals = ingredients[:, :-1]
cals = ingredients[:,-1]

def score_recipe(properties, recipe):
    prop_scores = (properties * recipe).sum(axis=1)
    return np.product(prop_scores[prop_scores >= 0])

score_recipe(ingredients_no_cals.T, [1, 2, 3, 4])

print("Rätsel 1:", max(score_recipe(ingredients_no_cals.T, rcpe) for rcpe in generate_recipes()))

def check_cals(cals, recipe):
    return (cals * recipe).sum() == 500

print(
    "Rätsel 2:", 
    max(
        score_recipe(ingredients_no_cals.T, rcpe) 
        for rcpe in generate_recipes()
        if check_cals(cals, rcpe)
    )
)
