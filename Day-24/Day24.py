from itertools import combinations
from functools import reduce
from operator import mul
with open('input.txt', 'r') as f:
    weights = [int(line.strip('\n')) for line in f.readlines()]
    f.close()
total_weight = sum(weights)
#math works out so that given compartment 1 = goal weight, the oher compartments can be made the goal weight as well
def find_qe(compartments):
    goal_weight = total_weight//compartments
    for i in range(len(weights)):
        qes = [reduce(mul, combo) for combo in combinations(weights, i) if sum(combo) == goal_weight]
        if qes: return min(qes)

print(find_qe(3), find_qe(4))