import re
pattern = r'on|off|toggle|\d{1,3}' #takes out nonsense and leaves on/off/toggle and each number for start stop
with open('input_6.txt', 'r') as file:
    directions = [re.findall(pattern, line.strip('\n')) for line in file.readlines()]
file.close()
import numpy as np

# Part 1 
# 0 = off and 1 = on
def do_something(mat, start, stop, direction):
    match direction:
        case 'on':
            mat[start[0]:stop[0]+1,start[1]:stop[1]+1] = 1
        case 'off':
            mat[start[0]:stop[0]+1,start[1]:stop[1]+1] = 0
        case 'toggle':
            temp = mat[start[0]:stop[0]+1, start[1]:stop[1]+1]
            temp = np.where(temp < 1, 1, 0)
            mat[start[0]:stop[0]+1,start[1]:stop[1]+1] = temp

lights = np.zeros([1000, 1000])
for dir in directions:
    do_something(lights, [int(dir[1]), int(dir[2])], [int(dir[3]), int(dir[4])], dir[0])
print(int(sum(lights.flatten())))

#Part 2
def do_something_else(mat, start, stop, direction):
    match direction:
        case 'on': #inc by 1
            temp = mat[start[0]:stop[0]+1, start[1]:stop[1]+1]+1
            mat[start[0]:stop[0]+1,start[1]:stop[1]+1] = temp
        case 'off': 
            temp = mat[start[0]:stop[0]+1, start[1]:stop[1]+1]-1
            temp = np.where(temp < 0, 0, temp)
            mat[start[0]:stop[0]+1,start[1]:stop[1]+1] = temp
            
        case 'toggle':
            temp = mat[start[0]:stop[0]+1, start[1]:stop[1]+1]+2
            mat[start[0]:stop[0]+1,start[1]:stop[1]+1] = temp
brights = np.zeros([1000,1000])
for dir in directions:
    do_something_else(brights, [int(dir[1]), int(dir[2])], [int(dir[3]), int(dir[4])], dir[0])
print(int(sum(brights.flatten())))