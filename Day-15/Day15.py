sugar, sprinkles, candy, chocolate = [3, 0, 0,-3, 2], [-3, 3, 0,0, 9], [-1, 0, 4, 0, 1], [0, 0, -2, 2, 8]
#ended up doing manual input
tsp, high_score, calorie_hs = 100, 0, 0
#nested for loops never surpass 100 tsp total, goes through every combo
for sug in range(tsp+1): #0-100
    for sprink in range(tsp+1-sug): #0 to 100-sprink
        for can in range(tsp+1-sprink-sug): #0 to 100-sprink-sug
            for choc in range (tsp+1-can-sprink-sug): #0 to 100-can-sug-sprink
                if sum([sug, sprink, can, choc]) == tsp: #ig the total is 100
                    cap = sugar[0]*sug + sprinkles[0]*sprink + candy[0]*can + chocolate[0]*choc
                    dur = sugar[1]*sug + sprinkles[1]*sprink + candy[1]*can + chocolate[1]*choc
                    flav = sugar[2]*sug + sprinkles[2]*sprink + candy[2]*can + chocolate[2]*choc
                    texture = sugar[3]*sug + sprinkles[3]*sprink + candy[3]*can + chocolate[3]*choc
                    if cap < 0 or dur <0 or flav < 0 or texture < 0:
                        total = 0
                    else:
                        total = cap*dur*flav*texture
                        if sum([sugar[-1]*sug, sprinkles[-1]*sprink, candy[-1]*can, chocolate[-1]*choc]) == 500:
                               calorie_hs = max(calorie_hs, total)
                    high_score = max(high_score, total )
print(high_score) #part 1
print(calorie_hs) #part 2