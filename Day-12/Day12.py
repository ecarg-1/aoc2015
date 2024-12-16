import re
with open('input.txt', 'r') as file:
    text = file.read()
file.close()
#Part 1
print(sum([int(i) for i in re.findall(r'\d{1,3}|-\d{1,3}', text)]))

no_red = re.sub(r'{', '', text)
print(no_red)