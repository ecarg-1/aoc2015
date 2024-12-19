import math
input = 33100000

house, presents = 0, 0
def factor(num, part):
    a = [i for i in range(1, int(math.sqrt(num))+1) if num%i==0]
    b = [num/i for i in a if i*i!=num]
    if part == 1:
        return sum(a+b)
    else:
        return a+b
part1, part2 = False, False
while(not part1 or not part2):
    house+=1
    if 10 * factor(house, 1) >= input and not part1:
        print(house)
        part1 = True
    if sum([i for i in factor(house, 2) if house/i <=50]) * 11 >= input and not part2:
        print(house)
        part2 = True


