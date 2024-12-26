inp = [[list(y.strip()) for y in x.split("\n") ] for x in  open("in").read().strip().split("\n\n")]

# Transpose the input nested lists
inp = [([list(x) for x in zip(*y)]) for y in inp]



def convert_to_heights(grid):
    hs = []
    l = len(grid[0])-1
    for row in grid:
        h = row.count("#")-1
        hs.append(h)
        
    return (l, hs)


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()
    
def is_compatible(key, lock):
    l = key[0]
    for n in range(len(key[1])):
        if key[1][n] + lock[1][n] >= l:
            return False
    return True
    



keys = []
locks = []
for i in inp:
    if i[0][0] == ".":
        keys.append(convert_to_heights(i))
    else:
        locks.append(convert_to_heights(i))
        
        
        
comp = []
for key in keys:
    for lock in locks:
        if is_compatible(key, lock):
            comp.append((key, lock))
            
print(len(comp))