with open('input.txt', 'r') as f:
    stats = [line.split(' ') for line in f.readlines()]
f.close()
import math
my_dict = {s[0]: [int(s[3]), int(s[6]), int(s[-2])] for s in stats}
secs = 2503
def distance (total_time, speed, active, rest):
    cycle_time = active + rest
    distance = math.floor(total_time/cycle_time)*speed*active 
    remaining_time = total_time % cycle_time
    if remaining_time >= active:
        distance += active*speed
    else:
        distance += remaining_time*speed
    return distance

max_dist = 0
for value in my_dict.values():
    dist = distance(secs, value[0], value[1], value[2])
    if dist > max_dist:
        max_dist=dist
print(max_dist)

points = {s[0]: 0 for s in stats}

for second in range(1, secs+1):
    distance_dict = dict()
    for keys, values in my_dict.items():
        d = distance(second, values[0], values[1], values[2])
        if d not in distance_dict.keys():
            distance_dict[d] = [keys]
        else:
            distance_dict[d].append(keys)
    furthest = max([d for d in distance_dict.keys()])
    for reindeer in distance_dict[furthest]:
        points[reindeer]+=1
print(max(d for d in points.values()))