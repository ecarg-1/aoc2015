import numpy as np
import operator 
with open ("input.txt", "r") as file:
    commands = [line.strip('\n').split(' ') for line in file.readlines()]
file.close()
with open ("test.txt", "r") as file:
    tests = [line.strip('\n').split(' ') for line in file.readlines()]
file.close()
ops = {'AND': operator.and_, 'OR': operator.or_, 'NOT': operator.inv, 'LSHIFT': operator.lshift, 'RSHIFT': operator.rshift}
wires = {}

def do_something(c): #intakes one command line
    l = len(c)
    skipped = False
    match l:
        case 5: #and or lshift rshift
            try:
                wires[c[-1]] = ops[c[1]](wires[c[0]], wires[c[2]]) #adds wire c[-1] to dictionary using wires from dictionary already
            except KeyError:
                try:
                    wires[c[-1]] = ops[c[1]](wires[c[0]], int(c[2])) #adds wire c[-1] to dictionary using wire from dict and int
                except:
                    try:
                        wires[c[-1]] = ops[c[1]](int(c[0]), wires[c[2]]) #adds wire c[-1] to dictionary using int and wire from dict
                    except:
                        skipped = True
                        pass
        case 4: #not
           try:
               wires[c[-1]] = ops[c[0]](np.uint16(wires[c[1]])) #adds wire c[-1] to dict using wire val from dict (also assigns int 16 bits)
           except KeyError:
                try:
                    wires[c[-1]] = ops[c[0]](np.uint16(int(c[1]))) #adds wire c[-1] to dict using 16 bit int
                except:
                    skipped = True
                    pass
        case 3: #no op
            try:
                r = int(c[0]) #try to set the right number to c[0]
                wires[c[2]] = r #the wire c[2] is then assigned the number c[0] if it exists
            except ValueError: #if c[0] is not a number
                try:
                    r = wires[c[0]] #try to set the right number to something from the dictionary
                    wires[c[2]]=r #assigns the wire c[2] the value from the dictionary
                except: #skips if nothing can happen
                    skipped = True
                    pass
    return skipped

while(True):
    if len(commands) == 0: #once each command has been added to dict, done
        break
    for c in commands: #goes through commands 
        if not do_something(c): #if the line was not skipped over,
            commands.remove(c) #removes the line out
print(wires['a'])
