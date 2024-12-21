import itertools 
from functools import reduce
from operator import mul
with open('input.txt', 'r') as f:
    weights = [int(line.strip('\n')) for line in f.readlines()]
    f.close()

def do_something(packages, stage, size): #returns min size of the packages in the front
    min_qe = 0
    for i in range(1, len(packages)): #starts at 1 (combo will have at least 1), ends at len(package) (leftover will have at least 1) 
        fcc = list(itertools.combinations(packages, i)) if stage == 1 else list(itertools.combinations(packages, size))
        #1st compartment combos starting with 1 package and incrementing/combos of given size
        for c1 in fcc: #iterates through each combination
            leftover1 = list(set(packages) - set(c1)) #original list - combos leaves leftovers
            if sum(leftover1) == 2*sum(c1): #ignores if it cannot make an equal list
                for j in range(0, len(leftover1)): #repeats for finding second compartment
                    scc = list(itertools.combinations(leftover1, j)) #second compartment combos
                    for c2 in scc:
                        c3 = list(set(leftover1) - set(c2)) #leftover1 - combos leaves leftovers (third compartment)
                        if sum(c1) == sum(c2) == sum(c3):
                            if stage == 1: return len(c1) #this is the shortest length of c1 
                            else:
                                print(c1)
                                min_qe = reduce(mul, c1) if min_qe == 0 else min(reduce(mul, c1),min_qe)
                                break
                if stage != 1: break
        if stage != 1: return min_qe      

def do_something_else(packages, stage, size): #returns min size of the packages in the front
    min_qe = 0
    for i in range(1, len(packages)): #starts at 1 (combo will have at least 1), ends at len(package) (leftover will have at least 1) 
        fcc = list(itertools.combinations(packages, i)) if stage == 1 else list(itertools.combinations(packages, size))
        #1st compartment combos starting with 1 package and incrementing/combos of given size
        for c1 in fcc: #iterates through each combination
            leftover1 = list(set(packages) - set(c1)) #original list - combos leaves leftovers
            if sum(leftover1) == 3*sum(c1): #ignores if it cannot make an equal list
                for j in range(1, len(leftover1)+1): #repeats for finding second compartment
                    scc = list(itertools.combinations(leftover1, j)) #second compartment combos
                    for c2 in scc:
                        leftover2 = list(set(leftover1) - set(c2)) #leftover1 - combos leaves leftovers
                        if sum(c1) == sum(c2): #ignore invalid ones
                            print('um')
                            for k in range(1,len(leftover2)+1):
                                tcc = list(itertools.combinations(leftover2, k)) #third compartment combos
                                for c3 in tcc:
                                    c4 = list(set(leftover2) - set(c3))
                                    if sum(c1) == sum(c2) == sum(c3) == sum(c4):
                                        print(c1,c2,c3,c4) 
                                        if stage == 1: return len(c1) #this is the shortest length of c1
                                        else:
                                            min_qe = reduce(mul, c1) if min_qe == 0 else min(reduce(mul, c1),min_qe)
                                            
                                            break
                            if stage != 1:break
                    if stage != 1: break
                if stage != 1: return min_qe        
# size = do_something(weights, 1, None)
# size2 = do_something_else(weights, 1, None)
# print(do_something(weights, 2, size), do_something_else(weights, 2, size2))
# print(do_something_else(weights, 2, 5))

def min_size(packages, compartments, stage, size): 
    x = 2 if compartments == 3 else 3
    min_qe = 0
    c1_list = []
    for i in range(1, len(packages)): 
        fcc = list(itertools.combinations(packages, i)) if stage == 1 else list(itertools.combinations(packages, size))
        for c1 in fcc: 
            leftover1 = list(set(packages) - set(c1)) 
            if sum(leftover1) == x*sum(c1):
                for j in range(0, len(leftover1)+1):
                    scc = list(itertools.combinations(leftover1,j))
                    for c2 in scc:
                        leftover2 = list(set(leftover1)-set(c2)) #aka c3
                        if compartments == 3:
                            if sum(c1) == sum(c2) == sum(leftover2):
                                if stage == 1: return len(c1)
                                else: 
                                    min_qe = reduce(mul, c1) if min_qe == 0 else min(min_qe, reduce(mul, c1))
                                    c1_list.append(c1)
                                #print(min_qe, 'c1', c1)
                        else:
                            if sum(leftover2) == sum(c1)+sum(c2):
                                for k in range(0, len(leftover2)+1):
                                    tcc = list(itertools.combinations(leftover2, k))
                                    for c3 in tcc:
                                        c4 = list(set(leftover2)-set(c3))
                                        if sum(c1)==sum(c2)==sum(c3)==sum(c4):
                                            if stage == 1: return len(c1)
                                        #if stage != 1: break
                                    #if stage != 1: break
                        if stage != 1 and c1 in c1_list: break
                    #if stage != 1: break
    return min_qe

                            
print(do_something(weights, 2, 6))
