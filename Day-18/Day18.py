with open ('input.txt','r') as f:
    grid = [line.strip('\n') for line in f.readlines()]
    f.close()
#grid = ['.#.#.#', '...##.','#....#','..#...','#.#..#','####..']
size = len(grid)
def border(grid):
    expanded_grid = []
    expanded_grid.append('.'*(size+2))
    for line in grid:
        expanded_grid.append('.'+line+'.')
    expanded_grid.append('.'*(size+2))
    return expanded_grid
def count_on(row,col, expanded_grid):
    cur_str = ''
    cur_str+=expanded_grid[row-1][col-1:col+2]
    cur_str+=expanded_grid[row+1][col-1:col+2]
    cur_str+=expanded_grid[row][col-1]
    cur_str+=expanded_grid[row][col+1]
    return cur_str.count('#')
        
def find_status(row,col, expanded_grid):
    ons = count_on(row,col, expanded_grid)
    if expanded_grid[row][col] == '#':
        if ons == 2 or ons == 3: result = '#'
        else: result = '.'
    else:
        if ons == 3: result = '#'
        else: result = '.'
    return result

def update(grid):
    old_grid = border(grid)
    new_grid = []
    for r in range(1,size+1):
        cur_row = ''
        for c in range(1,size+1):
            cur_row+=find_status(r,c,old_grid)
        new_grid.append(cur_row)
    return new_grid
def turn_corners_on(grid):
    new_grid = []
    new_grid.append('#'+grid[0][1:-1]+'#')
    for i in range(1,size-1):
        new_grid.append(grid[i])
    new_grid.append('#'+grid[size-1][1:-1]+'#')
    return new_grid
# for i in range(100):
#     grid = update(grid)
# print(sum(line.count('#') for line in grid))
grid = turn_corners_on(grid)
for i in range(100):
    grid = update(grid)
    grid = turn_corners_on(grid)
print(sum(line.count('#') for line in grid))