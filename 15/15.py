inp = open('in').read().split('\n\n')

stuff = [list(x) for x in inp[0].split('\n')]

actions = list(inp[1].replace('\n', ''))


cur_pos = (0, 0)
# boxes = []
# walls = []
for i in range(len(stuff)):
    for j in range(len(stuff[0])):        
        if stuff[i][j] == '@':
            cur_pos = (i, j)

def print_map():
    for i in range(len(stuff)):
        for j in range(len(stuff[0])):
            print(stuff[i][j], end='')
        print()
        
        
dirs = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

def move(y, x, direction, grid):
    cur_sign = grid[y][x]
    if cur_sign == '.':
        return True
    if cur_sign == '#':
        return False
    next_y, next_x = y + dirs[direction][0], x + dirs[direction][1]
    
    if move(next_y, next_x, direction, grid):
        next_sign = grid[next_y][next_x]
        grid[next_y][next_x] = cur_sign
        grid[y][x] = next_sign
        return True
    
    return False


for i, action in enumerate(actions):
    if move(cur_pos[0], cur_pos[1], action, stuff):
        cur_pos = (cur_pos[0] + dirs[action][0], cur_pos[1] + dirs[action][1])
    
score = 0
for i in range(len(stuff)):
    for j in range(len(stuff[0])):
        if stuff[i][j] == 'O':
            score += 100*i +j
        
print(score)