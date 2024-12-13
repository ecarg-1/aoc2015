with open("input_5.txt", "r") as file:
    strings = [line.strip('\n') for line in file.readlines()]
file.close()
#Part 1
#Requirements
#Has at least 3 vowels (aeiou)
#Has at least 1 set of double letters
#Does not contain ab cd pq xy

#Info: a=97 z=122
bad_combos = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
nice_count = 0
for s in strings:
    status = 'nice'
    vowel_count = 0
    double_count = 0
    for combo in bad_combos:
        if combo in s:
            status = 'naughty'
    for vowel in vowels:
        vowel_count = vowel_count + s.count(vowel)
    for letter in range(97, 123):
        double_count = double_count + s.count(2*chr(letter))
    if vowel_count < 3 or double_count < 1:
        status = 'naughty'
    if status == 'nice':
        nice_count = nice_count + 1
print(nice_count)

#Part 2
#Requirements
#Pair of any 2 letters that repeats at least twice w/o overlap
#Contains one letter that repeats with one letter between
import re
nc = 0
for s in strings:
    stat = 'naughty' 
    pair, x_x = False, False
    for i in range(len(s)-1):
        pattern = s[i:i+2]
        matches = re.findall(pattern, s)
        if len(matches)>1:
            pair = True
            break
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            x_x = True
    if  pair and x_x:
        stat = 'nice'
    if stat == 'nice':
        nc = nc + 1
print(nc)