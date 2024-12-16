with open ('input.txt', 'r') as f:
    h = [line.strip('.\n').split(' ') for line in f.readlines()]
f.close()
people = list(set([s[0] for s in h]))
import itertools
perms = list(itertools.permutations(people)) #list of all possible orders
happiness_units = {(s[0], s[-1]): (int(s[3]) if s[2]=='gain' else -int(s[3])) for s in h} #list of happiness gained by a when sitting next to b

def happiness(perms):
    max_happiness = 0
    for seating_arrangement in perms:
        #adds first and last person in loop to start
        if seating_arrangement[0] != 'Me' and seating_arrangement[-1] != 'Me':
            cur_happiness = happiness_units[(seating_arrangement[0], seating_arrangement[-1])] + happiness_units[(seating_arrangement[-1], seating_arrangement[0])]
        else: #if firt/last person is me then it's 0
            cur_happiness = 0
        for i in range(len(seating_arrangement)-1):
            if seating_arrangement[i] != 'Me' and seating_arrangement[i+1] != 'Me':
                cur_happiness += (happiness_units[(seating_arrangement[i], seating_arrangement [i+1])] + happiness_units[(seating_arrangement[i+1], seating_arrangement[i])])
        if cur_happiness > max_happiness:
            max_happiness = cur_happiness
    return max_happiness

#Part 1
print(happiness(perms))
#Part 2
people.append('Me') #Adding me to the list
perms_with_me = list(itertools.permutations(people)) #new list of all perms
print(happiness(perms_with_me))