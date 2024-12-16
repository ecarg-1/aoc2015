import re
import json
with open('input.txt', 'r') as file:
    text = file.read()
file.close()
#Part 1
print(sum([int(i) for i in re.findall(r'\d{1,3}|-\d{1,3}', text)]))
#Part 2
formatted_text = json.loads(text) #formats dictionary
def n(obj): #takes in an object (dict, list, int, or string) goal is to return an int
    if isinstance(obj, dict): #if object is a dictionary
        if "red" in obj.values(): #if red is in the dict, whole dict does not count
            return 0 #total is 0
        return sum([n(vals) for vals in obj.values()]) #go through each value (whether list, dict, int, or str) and return a total
    elif isinstance(obj, list): #if list
        return sum([n(item) for item in obj]) #go through each item in list (whether list, dict, int, or str) and return total
    elif isinstance(obj, int): #if int, returns int to be summed
        return obj
    else: #if string, adds 0
        return 0
print(n(formatted_text))