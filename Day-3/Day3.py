with open ("input_3.txt", "r") as file:
    text = file.read()
file.close()
#Part 1
def houses(dir):
    directions  = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    visited_houses = []
    position = (0,0)
    for d in dir:
        position = (position[0] + directions[d][0], position[1] + directions[d][1])
        visited_houses.append(position)
    return set(visited_houses)
print(len(houses(text)))
#Part 2
santa, robo_santa = text[0::2], text[1::2]
print(len(houses(santa).union(houses(robo_santa))))



