from collections import defaultdict
from time import sleep


inp = [x.strip().split(" ") for x in open('in').readlines()]

def p1(n):
    robots = defaultdict(list)
    rss = []


    for r in inp:
        # x, y
        pos = tuple([int(x) for x in r[0].replace("p=", "").split(",")])
        # vx, vy
        vel = tuple([int(x) for x in r[1].replace("v=", "").split(",")])
        
        robots[pos].append(vel)
        rss.append((pos, vel))
        
    min_y = 0
    max_y = 102
    min_x = 0
    max_x = 100

    n_steps = n


    def print_grid():
        grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        
        for r in rss:
            pos = r[0]
            grid[pos[1]][pos[0]] = grid[pos[1]][pos[0]]+1
        
        for row in grid:
            # if 0, print " ", else print "#"
            print("".join(["#" if x > 0 else "." for x in row]))
        
        print("\n\n")
    
    def write_grid_to_file():
        
        
        
        grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        
        for r in rss:
            pos = r[0]
            grid[pos[1]][pos[0]] = grid[pos[1]][pos[0]] + 1
            
        string = ""
        
        for row in grid:
            # if 0, print " ", else print "#"
            string += "".join(["#" if x > 0 else "." for x in row]) + "\n"
            
        # See if there are more than 5 # in a row
        rows = string.split("\n")
        found = False
        for i in range(len(rows)):
            if rows[i].find("######") != -1:
                found = True
                break
                
        
        if found:
            print("Found at n_steps: ", n_steps)
            with open(str(n)+"_out.txt", "w") as f:
                f.write(string)
            
        
        

    def wrap_around(pos):
        x, y = pos
        x = (x + max_x + 1) % (max_x + 1)
        y = (y + max_y + 1) % (max_y + 1)
        
        return (x, y)


    # For each robot, find out where after n_steps
    for i in range(len(rss)):
        r = rss[i]
        pos = r[0]
        vel = r[1]
        
        new_pos = (pos[0] + n_steps * vel[0], pos[1] + n_steps * vel[1])
        new_pos = wrap_around(new_pos)
        
        rss[i] = (new_pos, vel)


    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for r in rss:
        pos = r[0]
        
        if pos[0] > max_x // 2 and pos[1] < max_y // 2:
            q1 += 1
        elif pos[0] < max_x // 2 and pos[1] < max_y // 2:
            q2 += 1
        elif pos[0] < max_x // 2 and pos[1] > max_y // 2:
            q3 += 1
        elif pos[0] > max_x // 2 and pos[1] > max_y // 2:
            q4 += 1

    write_grid_to_file()
        
        
for i in range(10000):
    p1(i)