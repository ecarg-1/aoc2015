my_string = '1113222113'

def look_and_say(string):
    output = ''
    skips = 0
    for i in range(len(string)):
        if skips == 0:
            repeats = 1
            for j in range(i+1, len(string)):
                if string[i]==string[j]:
                    repeats+=1
                else:
                    break
            output += str(repeats) + string[i]
            skips = repeats-1
        else:
            skips-=1
    return output

for i in range(50):
    my_string = look_and_say(my_string)
    if i==39: #Part 1
        print(len(my_string))
    if i==49: #Part 2
        print(len(my_string))