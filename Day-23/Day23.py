with open('input.txt','r') as f:
    instructions = [line.strip('\n').split(' ') for line in f.readlines()]
    f.close()
a, b, i = 1, 0, 0 #both registers start at 0 and index starts at 0 or 1 depending on part 1 or 2
while(i < len(instructions)):
    ci = instructions[i] #current instruction
    match ci[0]:
        case 'inc':
            a = a + 1 if ci[1] == 'a' else a
            b = b + 1 if ci[1] == 'b' else b
        case 'hlf':
            a = int(a/2) if ci[1] == 'a' else a
            b = int(b/2) if ci[1] == 'b' else b
        case 'tpl':
            a = a*3 if ci[1] == 'a' else a
            b = b*3 if ci[1] == 'b' else b
        case 'jmp': 
            i = i + int(ci[1][1:]) - 1 if ci[1][0] == '+' else i - int(ci[1][1:]) - 1
        case 'jie': 
            if eval(ci[1][0])%2 == 0: i = i + int(ci[2][1:]) - 1 if ci[2][0] == '+' else i - int(ci[2][1:]) - 1
        case 'jio': 
            if eval(ci[1][0]) == 1: i = i + int(ci[2][1:]) - 1 if ci[2][0] == '+' else i - int(ci[2][1:]) - 1
    i+=1
print(b)
