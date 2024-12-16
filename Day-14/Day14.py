with open('input.txt', 'r') as f:
    stats = [line.split(' ') for line in f.readlines()]
f.close()
my_dict = {s[0]: [int(s[3]), int(s[6]), int(s[-2])] for s in stats}
print(my_dict)