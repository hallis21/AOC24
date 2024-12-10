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
            
            
ends = []
new_map_1 = []
new_map_2 = []
for i in range(0, len(inp)):
    new_map_1.append([])
    new_map_2.append([])
    for j in range(0, len(inp[i])):
        if inp[i][j] == 9:
            new_map_1[i].append([(i, j)])
            new_map_2[i].append([((i, j),)])
            ends.append((i, j))
        else:
            new_map_1[i].append([])
            new_map_2[i].append([])
            
            
def get_all_neighbours(coord):
    x, y = coord
    # filter out invalid coords
    # the number on the coord must be coord -1
    neighbours = []
    if x - 1 >= 0 and inp[x - 1][y] == inp[x][y] - 1:
        neighbours.append((x - 1, y))
    if x + 1 < len(inp) and inp[x + 1][y] == inp[x][y] - 1:
        neighbours.append((x + 1, y))
    if y - 1 >= 0 and inp[x][y - 1] == inp[x][y] - 1:
        neighbours.append((x, y - 1))
    if y + 1 < len(inp[x]) and inp[x][y + 1] == inp[x][y] - 1:
        neighbours.append((x, y + 1))
    return neighbours
        

    
def add_to_neighbours(coord, i):
    if i == 10:
        return
    for n in get_all_neighbours(coord):
        x, y = n
        new_path = [tuple(list(x)+[n]) for x in new_map_2[coord[0]][coord[1]]]
        new_map_1[x][y].extend(new_map_1[coord[0]][coord[1]])
        new_map_2[x][y].extend(new_path)
        add_to_neighbours(n, i+1)
        
for end in ends:
    add_to_neighbours(end,0 )
        

        

# Print the lens of all the trailheds
lens_1 = []
lens_2 = []
for t in trailheads:
    lens_2.append(len(set(new_map_2[t[0]][t[1]])))
    lens_1.append(len(set(new_map_1[t[0]][t[1]])))
    
print(sum(lens_2), sum(lens_1))