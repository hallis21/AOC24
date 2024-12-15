inp = open('in').read().split('\n\n')

stuff = [list(x) for x in inp[0].split('\n')]


replace = {
    '@': '@.',
    'O': '[]',
    '#': '##',
    '.': '..'
}
for i in range(len(stuff)):
    for j in range(len(stuff[0])):
        stuff[i][j] = list(replace[stuff[i][j]])
        
# flatten
for i in range(len(stuff)):
    stuff[i] = [x for sublist in stuff[i] for x in sublist]

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
    print()
        
        
dirs = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}


def is_legal_move(y, x, direction, grid):
    # do the same as move but without actually moving
    cur_sign = grid[y][x]
    if cur_sign == '.':
        return True
    if cur_sign == '#':
        return False
    next_y, next_x = y + dirs[direction][0], x + dirs[direction][1]
    sign_next = grid[next_y][next_x]
    if sign_next == '[' and direction in ['v', '^']:
        # try to move both  
        move_left = is_legal_move(next_y, next_x, direction, grid)
        move_right = is_legal_move(next_y, next_x+1, direction, grid)
        return move_left and move_right
    elif sign_next == ']' and direction in ['v', '^']:
        # try to move both  
        move_left = is_legal_move(next_y, next_x, direction, grid)
        move_right = is_legal_move(next_y, next_x-1, direction, grid)
        return move_left and move_right
    
    return is_legal_move(next_y, next_x, direction, grid)

def move(y, x, direction, grid):
    cur_sign = grid[y][x]
    if cur_sign == '.':
        return True
    if cur_sign == '#':
        return False
    next_y, next_x = y + dirs[direction][0], x + dirs[direction][1]
    sign_next = grid[next_y][next_x]
    
    should_move = is_legal_move(next_y, next_x, direction, grid)
    
    # if bracket, move both 
    if should_move:
        if sign_next == '[' and direction in ['v', '^']:
            # try to move both  
            move(next_y, next_x, direction, grid)
            move(next_y, next_x+1, direction, grid)
        elif sign_next == ']' and direction in ['v', '^']:
            # try to move both  
            move(next_y, next_x, direction, grid)
            move(next_y, next_x-1, direction, grid)
        
        else:
            move(next_y, next_x, direction, grid)
        next_sign = grid[next_y][next_x]
        grid[next_y][next_x] = cur_sign
        grid[y][x] = next_sign
        return True
    
    return False

for i, action in enumerate(actions):
    if is_legal_move(cur_pos[0], cur_pos[1], action, stuff) and move(cur_pos[0], cur_pos[1], action, stuff):
        cur_pos = (cur_pos[0] + dirs[action][0], cur_pos[1] + dirs[action][1])

print_map()
    
score = 0
for i in range(len(stuff)):
    for j in range(len(stuff[0])):
        if stuff[i][j] == '[':
            score += 100*i +j
        
print(score)