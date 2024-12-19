import itertools
with open('input.txt','r') as f:
    a = [line.strip('\n').split(' ') for line in f.readlines()]
f.close()
for i in range(len(a)): #for formatting
    a[i] = [x for x in a[i] if x!='']
#cost, dmg, armor
weapons = {i[0] : [int(i[1]), int(i[2]), int(i[3])] for i in a[1:6]}
armor = {i[0] : [int(i[1]), int(i[2]), int(i[3])] for i in a[8:13]}
armor['none'] = [0,0,0] #adds the option to have no armor to dict
rings = {i[0]+' '+i[1] : [int(i[2]), int(i[3]), int(i[4])] for i in a[15:]}
w_keys, a_keys, r_keys = weapons.keys(), armor.keys(), rings.keys()
two_ring = list(itertools.combinations(r_keys,2)) #all combinations of 2 rings
ring_combo = [0, 1, 2] #options for how many rings selected

def calculations(weap, arm, rin): #calcualtes the cost, damage, and armor based on the combination of items
    d, a, c = weapons[weap][1], armor[arm][2], weapons[weap][0] + armor[arm][0] #sets c,d,a from weapon and armor first (no ring totals)
    if isinstance(rin, tuple): #if there are 2 rings, updates totals
        d += sum([rings[i][1] for i in rin])
        a += sum([rings[i][2] for i in rin])
        c += sum([rings[i][0] for i in rin])
    elif isinstance(rin, str): #if there is 1 rings, updates totals
        d += rings[rin][1]
        a += rings[rin][2]
        c += rings[rin][0]
    return c, d, a 
        
def find_winner(d, a): #fings who the winner is based on players damage and armor
    boss_hp, player_hp = 103, 100
    boss_dmg, boss_armor = 9, 2
    player_dmg_delt = d-boss_armor if d-boss_armor > 0 else 1 #calculates how much dmg player deals
    boss_dmg_delt = boss_dmg - a if boss_dmg -a > 0 else 1 #calculates how much dmg boss deals
    while(True):
        boss_hp -= player_dmg_delt #starts with player and decrements boss's hp
        if boss_hp <= 0: return 'player' #checks to see if boss defeated and returns who won
        player_hp -= boss_dmg_delt #decrements players hp
        if player_hp <= 0: return 'boss' #checks to see if boss won and returns who won
min_cost = 10000000 #Part 1
max_cost = 0 #Part 2
for w in w_keys: #iterates through each weapon
    for a in a_keys: #iterates through each piece of armor
        for num in ring_combo: #iterates through number of rings
            if num==2: #iterates through 2 ring combos
                for r in two_ring:
                    cost, dmg, arm = calculations(w, a, r)
                    if find_winner(dmg, arm) == 'player': min_cost = min(cost, min_cost)
                    if find_winner(dmg, arm) == 'boss': max_cost = max(cost, max_cost)
            elif num==1: #iterates through 1 ring combos
                for r in r_keys:   
                    cost, dmg, arm = calculations(w, a, r)
                    if find_winner(dmg, arm) == 'player': min_cost = min(cost, min_cost)
                    if find_winner(dmg, arm) == 'boss': max_cost = max(cost, max_cost)
            else: #no ring combos
                cost, dmg, arm = calculations(w, a, 0)
                if find_winner(dmg, arm) == 'player': min_cost = min(cost, min_cost)
                if find_winner(dmg, arm) == 'boss': max_cost = max(cost, max_cost)
print(min_cost)
print(max_cost)