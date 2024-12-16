with open ('input.txt') as file:
    strings = [line.strip('\n') for line in file.readlines()]
file.close()
#part 1
non_esc_l, esc_l = 0, 0
for line in strings:
    non_esc_l += len(line)
    esc_l += len(eval(line))
print(non_esc_l-esc_l)
#part 2
import re
encode = 0
for line in strings:
    line = re.sub(r'\\', r'\\\\', line )
    line = '\"' + re.sub(r'"', r'\\"', line) + '\"'
    encode += len(line)
print(encode-non_esc_l)