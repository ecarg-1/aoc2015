import re
with open('input.txt','r') as f:
    info = [re.split(r',|:', line.strip('\n')) for line in f.readlines()]
    f.close()
my_dict = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
sue_dict = dict()
for sue in info:
    sue_dict[int(sue[0][4:])] = {sue[i+1][1:] : int(sue[i+2]) for i in  range (0 ,int(len(sue))-1, 2)}
for keys, values in sue_dict.items():
    flag, f2 = True, True
    for k, v in values.items():
        if v != my_dict[k]:
            flag = False
        if k == 'cats' or k=='trees':
            if v <= my_dict[k]:
                f2=False
        elif k =='pomeranians' or k == 'goldfish':
            if v>= my_dict[k]:
                f2=False
        else:
            if v!=my_dict[k]:
                f2=False
    if flag:
        print(keys)
    if f2:
        print(keys)


