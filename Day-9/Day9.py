with open('input.txt', 'r') as file:
    info = [line.strip('\n').split(' ') for line in file.readlines()]
file.close()
#part 1 and 2
import itertools
locations = list(set([d[0] for d in info]).union(set([d[2] for d in info]))) #gets unique list of locations
distances = {(d[0], d[2]): int(d[-1]) for d in info} #get distances between each location in dictionary so i can use keys to index 
perm = list(itertools.permutations(locations)) #makes a list of every permuatation
min_dist, max_dist = 0, 0
for route in perm:
    cur_dist = 0
    for i in range(len(route)-1):
        try: #since they keys are tuples tries (a,b)
            cur_dist += distances[(route[i], route[i+1])] #adds distance to total current distance
        except KeyError: #if that doesn't work then tries (b,a) to get distance
            cur_dist += distances[(route[i+1],route[i])]
    if min_dist==0 or cur_dist < min_dist:
        min_dist = cur_dist
    if max_dist < cur_dist:
        max_dist = cur_dist
print(min_dist, max_dist)

