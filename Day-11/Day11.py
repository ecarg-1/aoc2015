my_string = 'hepxcrrq'
#increments strings and wraps characters when needed
def increment(string):
    int_string = [ord(char) for char in string] #creates list of ascii for each char
    int_string[-1]+=1 #increments last ascii
    for i in range(1, len(string)): #goes through each ascii
        if int_string[-i]>122: #if it inc past z
            int_string[-i]=97 #wraps to a
            int_string[-i-1]+=1 #and incs the next ascii and repeats if inc past z
    return ''.join([chr(num) for num in int_string]) #joins the list of chars to a string

def valid_pass(string):
    if 'i' in string or 'o' in string or 'l' in string:
        return False
    int_string = [ord(char) for char in string]
    straight, pair_count = False, 0
    for i in range(len(int_string)-2):
        if int_string[i+2]-int_string[i+1] == 1 and int_string[i+1] - int_string[i] == 1:
            straight = True
    for i in range(97, 123):
        if 2*chr(i) in string:
            pair_count+=1
    if pair_count > 1 and straight:
        return True
    else:
        return False

def find_pass(password):
    while(True):
        password = increment(password)
        if valid_pass(password):
            return password

#Part 1
print(find_pass(my_string))
#Part 2
print(find_pass(find_pass(my_string)))