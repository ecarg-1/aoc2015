import itertools 
from functools import reduce
from operator import mul
with open('input.txt', 'r') as f:
    weights = [int(line.strip('\n')) for line in f.readlines()]
    f.close()

def min_size(packages): #returns min size of the packages in the front
    for i in range(1, len(packages)): #starts at 1 (combo will have at least 1), ends at len(package) (leftover will have at least 1) 
        fcc = list(itertools.combinations(packages, i)) #1st compartment combos starting with 1 package and incrementing
        for c1 in fcc: #iterates through each combination
            leftover1 = list(set(packages) - set(c1)) #original list - combos leaves leftovers
            if sum(leftover1) == 2*sum(c1): #ignores if it cannot make an equal list
                for j in range(1, len(leftover1)): #repeats for finding second compartment
                    scc = list(itertools.combinations(leftover1, j)) #second compartment combos
                    for c2 in scc:
                        c3 = list(set(leftover1) - set(c2)) #leftover1 - combos leaves leftovers (third compartment)
                        if sum(c1) == sum(c2) == sum(c3):
                           return len(c1) #this is the shortest length of c1 
                           


                            
print(combo(weights))
