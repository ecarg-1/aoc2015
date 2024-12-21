import random
spells = ['mm', 'd', 's', 'p', 'r'] #all possible spells
def play(part):
    player, mana, boss, mana_used, shield, recharge, poison, i = 50, 500, 51, 0, 0, 0, 0, 0
    while(True): 
        if i%2==0 and part: #only runs for part 2, on players turn before any effects, subtracts 1 hp
            player -= 1
            if player < 1 or mana < 1: return 'boss', mana_used #if player dies, exits
        if shield > 0: #tracks shield timer
            shield -= 1 #decrements
            armor = 7 #sets armor to 7 if sheild timer is active
        else: armor = 0#otherwise 0
        if recharge > 0:
            recharge -= 1
            mana += 101 #adds 101 mana when recharge is active
        if poison > 0:
            poison -= 1
            boss -= 3 #3 dmg when poison active
        if boss < 1: return 'player', mana_used #checks if boss died from any effects at start of players turn
        if i%2==0: #if it's player's turn
            spell = random.choice(spells) #picks a spell randomly
            match spell: #matches spell, adds/subtracts manas and does dmg or resotres hp for each spell
                case 'mm':
                    mana -= 53
                    mana_used += 53
                    boss -= 4
                case 'd': 
                    mana -= 73
                    mana_used += 73
                    boss -= 2
                    player += 2
                case 's':
                    shield += 6
                    mana -= 113
                    mana_used += 113
                case 'p':
                    poison += 6
                    mana -= 173
                    mana_used += 173
                case 'r':
                    recharge += 5
                    mana -= 229
                    mana_used += 229
            if mana < 1: return 'boss', mana_used #checks if player used all mana
            if boss < 1: return 'player', mana_used #checks if boss died
        else: player -= 9 - armor #boss turn, deals 9 or 9-7(armor) dmg to player
        if player < 1: return 'boss', mana_used #checks if player hp <= 0
        i+=1 #iterates i
min_pt1, min_pt2 = 100000, 10000
for i in range(1000000):
    a = play(False)
    b = play(True)
    if a[0] == 'player': min_pt1 = min(min_pt1, a[1])
    if b[0] == 'player': min_pt2 = min(min_pt2, b[1])
print(min_pt1, min_pt2)


