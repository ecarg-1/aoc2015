import re
with open("input_2.txt", "r") as file:
    lwh = file.read()
file.close()
#Part 1
pattern = r"(\d{1,2})x(\d{1,2})x(\d{1,2})"
lwh_numbers = re.findall(pattern, lwh)
count=0
for m in lwh_numbers:
    areas = [2*int(m[0])*int(m[1]), 2*int(m[1])*int(m[2]), 2*int(m[2])*int(m[0])]
    count = count+ sum(areas) + int(min(areas)/2)
print(count)
#Part 2
length = 0
for m in lwh_numbers:
    sides = [int(m[0]), int(m[1]), int(m[2])]
    sides.sort()
    length = length + 2*sum(sides[:-1]) + sides[0]*sides[1]*sides[2]

print(length)