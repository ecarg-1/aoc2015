row, col = 2981, 3075
def code_num(row,col): #returns what number code is at a given index
    cur_row, cur_col, cur_code = 1, 1, 1 #the code at 1,1 is the first code
    while cur_col < col: 
        cur_col += 1 
        cur_code += cur_col
    while cur_row < row:
        cur_code += cur_col + cur_row - 1
        cur_row += 1
    return cur_code
def code(num):
    start = 20151125
    for i in range(1, num):
        start = (start*252533)%33554393
    return start
print(code(code_num(row,col)))

