with open('input.txt','r') as f:
    containers = [int(line) for line in f.readlines()]
    f.close()
from itertools import combinations

amount = 150
total, min, min_total = 0, 0, 0
for c in range(len(containers)+1):
    combos = list(combinations(containers, c))
    for co in combos:
        if sum(co) == amount:
            total+=1
            if min==0:
                min = len(co)
            if len(co) == min:
                min_total+=1
print(total, min_total)