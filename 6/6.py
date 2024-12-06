inp = [list(x.strip()) for x in open("inp").readlines()]

obstacles = []

guard = None
# x, y
current_dir = (0, -1) # up

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] == "#":
            obstacles.append((x, y))
        if inp[y][x] == "^":
            guard = (x, y)
            
guard_copy = (guard[0], guard[1])
obstacles_copy = obstacles[:]

def get_next_coord(x, y, direction):
    next = (x + direction[0], y + direction[1])
    if next in obstacles:
        ## Turn 90 degrees to the right
        if direction == (0, -1):
            direction = (1, 0)
        elif direction == (1, 0):
            direction = (0, 1)
        elif direction == (0, 1):
            direction = (-1, 0)
        elif direction == (-1, 0):
            direction = (0, -1)
            
        next, direction = get_next_coord(x, y, direction)
        
    return next, direction

unique_visited = set()

# While inside the bounds
while guard[0] >= 0 and guard[0] < len(inp[0]) and guard[1] >= 0 and guard[1] < len(inp):
    unique_visited.add(guard)
    guard, current_dir = get_next_coord(guard[0], guard[1], current_dir)
    
print(len(unique_visited))
visited_dir = set()
    

loops = 0
for i, visited in enumerate(unique_visited):
    # Print progress
    if i % 100 == 0:
        print(i / len(unique_visited))
    
    # Add the coordinates to the obstacles
    # See if we end up in a loop
    guard = (guard_copy[0], guard_copy[1])
    current_dir = (0, -1)
    obstacles = obstacles_copy[:]
    obstacles.append(visited)
    
    # Only check
    
    visited_dir = set()
    
    while guard[0] >= 0 and guard[0] < len(inp[0]) and guard[1] >= 0 and guard[1] < len(inp):
        if (guard, current_dir) in visited_dir:
            loops += 1
            break
        
        visited_dir.add((guard, current_dir))
        guard, current_dir = get_next_coord(guard[0], guard[1], current_dir)
print(loops)