import hashlib

key = "ckczppom"

def find_ans (key, zeros):
    i = 0
    while (True):
        hex = hashlib.md5((key + str (i)).encode()).hexdigest() #adds number in str form to end of key and finds hex of md5
        if hex[:zeros] == zeros*'0':
            return i
        i = i + 1
    
#Part 1
print(find_ans(key, 5))
#Part 2
print(find_ans(key, 6))