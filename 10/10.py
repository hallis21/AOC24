inp = [[int(y) for y in list(x.strip())] for x in open("in").readlines()]



cur_coord = (0, 0)


trailheads = []

# for i in range(0, len(inp)):
#     if inp[i][0] == 0:
#         trailheads.append((i, 0))
#     if inp[i][len(inp[i]) - 1] == 0:
#         trailheads.append((i, len(inp[i]) - 1))
        
# for i in range(0, len(inp[0])):
#     if inp[0][i] == 0:
#         trailheads.append((0, i))
#     if inp[len(inp) - 1][i] == 0:
#         trailheads.append((len(inp) - 1, i))

for i in range(0, len(inp)):
    for j in range(0, len(inp[i])):
        if inp[i][j] == 0:
            trailheads.append((i, j))
        
trails = []

visited = {}

def get_all_neighbours(coord):
    x, y = coord
    # filter out invalid coords
    # the number on the coord must be coord +1 
    neighbours = []
    if x - 1 >= 0 and inp[x - 1][y] == inp[x][y] + 1:
        neighbours.append((x - 1, y))
    if x + 1 < len(inp) and inp[x + 1][y] == inp[x][y] + 1:
        neighbours.append((x + 1, y))
    if y - 1 >= 0 and inp[x][y - 1] == inp[x][y] + 1:
        neighbours.append((x, y - 1))
    if y + 1 < len(inp[x]) and inp[x][y + 1] == inp[x][y] + 1:
        neighbours.append((x, y + 1))
    return neighbours
    

def walk(coord, path, i):
    

    
    x, y = coord
    if x < 0 or x >= len(inp) or y < 0 or y >= len(inp[x]):
        return None
    if coord in path:
        return None
    
    if inp[x][y] == 9:
        return [path]
    
    neighbours = get_all_neighbours(coord)
    possible_paths = []
    for n in neighbours:
        p = walk(n, path + [coord], i+1)
        if p:
            visited[coord] = p
            possible_paths.extend(p)
    
    return possible_paths

    
paths = []
for t in trailheads:
    ps = walk(t, [], 0)
    
    endpoints = set()
    for p in ps:
        print(p)
        endpoints.add(p[-1])
    paths.append(endpoints)
        
        
    
    

print(paths)