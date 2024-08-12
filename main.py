import pandas as pd
import itertools

class Paddler:
    def __init__(self, name, weight, side):
        self.name = name
        self.weight = weight
        self.side = side

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + ":" + str(self.weight)

def gen_lineups(roster):
    all_possible = []
    size = len(roster)

    for i in range(size):
         for comb in itertools.combinations(roster, i):
            for perm in itertools.permutations(comb):
                complement = tuple(set(roster) - set(perm))
                for complement_perm in itertools.permutations(complement):
                    all_possible.append((perm, complement_perm))

    return all_possible

def calc_weight(lineup):
    left = 0
    right = 0
    for p in lineup[0]:
        left += p.weight
    
    for p in lineup[1]: 
        right += p.weight
    
    final = [left, right]
    return final

def filter_lineups(lineups):
    updated_lineups = []

    for l in lineups:
        weights = calc_weight(l)
        diff = abs(weights[0] - weights[1])

        if diff < 50:
            updated_lineups.append(l)

    return updated_lineups

def print_lineups(lineups):
    for c in updated_lineups:
        weights = calc_weight(c)
        diff = weights[0] - weights[1]
        diff = abs(diff)
        print(c)
        print(str(weights[0]) + ":" + str(weights[1]) + "-> " + str(diff))

p1 = Paddler("B", 150, "L")
p2 = Paddler("J", 200, "R")
p3 = Paddler("A", 100, "R")
p4 = Paddler("C", 125, "L")

all = [p1, p2, p3, p4]

lineups = gen_lineups(all)

updated_lineups = filter_lineups(lineups)

print_lineups(updated_lineups)