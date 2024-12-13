with open("input_1.txt", "r") as file:
    text = file.readline()
file.close()

#Part 1 
print(text.count('(')-text.count(')'))

#Part 2
for i in range(len(text)):
    if (text[:i].count('(')-text[:i].count(')')==-1):
        print(i)
        break