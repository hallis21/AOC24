inp = [list(x.strip()) for x in open('in').readlines()]

global_start = None
global_end = None
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == 'S':
            global_start = (i, j)
        if inp[i][j] == 'E':
            global_end = (i, j)
            inp[i][j] = '.'
            
print(global_start, global_end)


current = global_start
step = 0

def print_grid(inp):
    for row in inp:
        for cell in row:
            print(f"{cell:2}", end=" ")
        print()
    print()
    
    
traversed = list()
    
while current != global_end:
    x, y = current
    traversed.append(current)
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(inp) and 0 <= ny < len(inp[0]) and inp[nx][ny] == '.':
            inp[x][y] = step
            step += 1
            current = (nx, ny)
            break
inp[current[0]][current[1]] = step
traversed.append(current)


def part1():
    cheats = []
    for coord in traversed:
        cur = inp[coord[0]][coord[1]]
        for nb in [((-1,0), (-2,0)), ((1,0), (2,0)), ((0,-1), (0,-2)), ((0,1), (0,2))]:
            wx, wy = nb[0]
            tx, ty = nb[1]
            # If first in bounds and is wall, "#"
            val1 = inp[coord[0]][coord[1]]
            if 0 <= coord[0] + wx < len(inp) and 0 <= coord[1] + wy < len(inp[0]) and inp[coord[0] + wx][coord[1] + wy] == '#':
                
                # If second is in traversed
                if (coord[0] + tx, coord[1] + ty) in traversed:
                    val2 = inp[coord[0] + tx][coord[1] + ty]
                    if val1 < val2:
                        cheats.append((val2-val1)-2)
                        
    # Count number of each cheat (the value)
    # from collections import Counter

    # c = Counter(cheats)
    # print(c)

    over_100 = [x for x in cheats if x >= 100]

    print(len(over_100))
        
        
def distance_to(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])




from collections import Counter
def part2():
    
    # (start, end, time_saved)
    cheats = []
    for coord in traversed:
        val1 = inp[coord[0]][coord[1]]
        for dest in traversed:
            val2 = inp[dest[0]][dest[1]]
            distance = distance_to(coord, dest)
            if val1 < val2+distance and distance <= 20:
                time_saved = (val2 - val1) - distance
                if time_saved > 1:
                    cheats.append((coord, dest, time_saved))
    


    over = 100
    over_x = [x[2] for x in cheats if x[2] >= over]
    # c = Counter([x[2] for x in cheats if x[2] >= 50])
    # # Print in order of time saved
    # entries = sorted(c.items(), key=lambda x: x[0])
    # for entry in entries:
    #     print(entry)
    
    print(len(over_x))
        
part1()    
part2()
