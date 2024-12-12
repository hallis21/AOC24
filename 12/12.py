inp = [[(x, False) for x in  list(x.strip()) ]for x in open('in').readlines()]


def get_adj(x, y, inp):
    adj = []
    # Get adjacents that are the same sign
    for i in range(-1, 2):
        for j in range(-1, 2):
            # not a diagonal
            if abs(i) == abs(j):
                continue
            if i == 0 and j == 0:
                continue
            if x+i < 0 or y+j < 0:
                continue
            try:
                if inp[x+i][y+j][0] == inp[x][y][0]:
                    adj.append((x+i, y+j))
            except:
                pass
    return adj
def get_adj_diag(x, y, inp):
    adj = []
    diag = []
    # Get adjacents that are the same sign
    for i in range(-1, 2):
        for j in range(-1, 2):
            # not a diagonal
            
            if i == 0 and j == 0:
                continue
            if x+i < 0 or y+j < 0:
                continue
            try:
                if inp[x+i][y+j][0] == inp[x][y][0]:
                    if abs(i) == abs(j):
                        diag.append((x+i, y+j))
                        continue
                    adj.append((x+i, y+j))
            except:
                pass
    return (adj, diag)

connected_components = []

# While there are still unvisited nodes

total_unvisited = len(inp)*len(inp[0])

while total_unvisited > 0:
    # Find a node that is unvisited
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if not inp[i][j][1]:
                # Found an unvisited node
                # Start a new connected component
                connected_components.append([])
                # Add the node to the connected component
                connected_components[-1].append((i, j))
                # Mark the node as visited
                inp[i][j] = (inp[i][j][0], True)
                total_unvisited -= 1
                # Get the adjacents
                adj = get_adj(i, j, inp)
                # While there are adjacents
                while len(adj) > 0:
                    # Get the first adjacent
                    x, y = adj.pop(0)
                    # If the adjacent is unvisited
                    if not inp[x][y][1]:
                        # Add it to the connected component
                        connected_components[-1].append((x, y))
                        # Mark it as visited
                        inp[x][y] = (inp[x][y][0], True)
                        total_unvisited -= 1
                        # Get the adjacents
                        adj += get_adj(x, y, inp)
                        


def calculate_area(connected_component, inp):
    area = 0
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if (i, j) in connected_component:
                area += 1
    return area





def calculate_permimeter(connected_component, inp):
    perimeter = 0
    edge_points = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if (i, j) in connected_component:
                adj, diag = get_adj_diag(i, j, inp)
                perimeter += 4 - len(adj)
                if 4 - len(adj) > 0:
                    edge_points.append((i, j))
    return (perimeter, edge_points)



def find_all_sides(connected_component, edge_points, inp):
    
    # represented by ((y,x), dir)
    # dir = 0 -> up, 1 -> right, 2 -> down, 3 -> left
    
    # for each edge point we see if there are open spaces around it
    # one open space -> 1 side, a single point can have 4 sides
    sides = set()
    for i in edge_points:
        x, y = i
        
        # we can count a side if there is an open space (in the component) in that direction
        # It can also be out of bounds
        
        # up
        if (x-1, y) not in connected_component:
            sides.add(((y, x), 0))
        # right
        if (x, y+1) not in connected_component:
            sides.add(((y, x), 1))
        # down
        if (x+1, y) not in connected_component:
            sides.add(((y, x), 2))
        # left
        if (x, y-1) not in connected_component:
            sides.add(((y, x), 3))
    
    return sides
                
                
def find_connected_sides(sides):
    # With a list of sides, find all sides that are next to each other and in the same direction
    side_stack = list(sides)
    
    connected_sides = []
    
    while len(side_stack) > 0:
        start_side = side_stack.pop(0)
        # print("STart", start_side, side_stack)
        current_line = [start_side]
        # Walk left and right if dir is horizontal (1, 3)
        # Walk up and down if dir is vertical (0, 2)
        
        if start_side[1] % 2 == 0:
            # Vertical
            # Walk up
            y, x = start_side[0]
            y -= 1
            while ((y, x), start_side[1]) in side_stack:
                current_line.append(((y, x), start_side[1]))
                
                # # Remove the side from the list
                side_stack.remove(((y, x), start_side[1]))
                
                y -= 1
            # Walk down
            y, x = start_side[0]
            y += 1
            while ((y, x), start_side[1]) in side_stack:
                current_line.append(((y, x), start_side[1]))
                side_stack.remove(((y, x), start_side[1]))
                y += 1

        else:
            # print("Horizontal")
            # Horizontal
            # Walk left
            y,x = start_side[0]
            x -= 1
            while ((y, x), start_side[1]) in side_stack:
                current_line.append(((y, x), start_side[1]))
                side_stack.remove(((y, x), start_side[1]))
                x -= 1
            # Walk right
            y,x = start_side[0]
            x += 1
            while ((y, x), start_side[1]) in side_stack:
                current_line.append(((y, x), start_side[1]))
                side_stack.remove(((y, x), start_side[1]))
                x += 1
            # print(current_line)
        connected_sides.append(current_line)
        
    return connected_sides


sides_example= {((0,0), 1), ((0,1), 1),((0,2), 1),((0,3), 1), ((1,0), 1), ((1,1), 1),((1,2), 1),((1,3), 1)}

# print(find_connected_sides(sides_example))

sums_p1 = 0
sums = 0

# Print each connected component print the whole board and mark the connected componenwith X
for ii, i in enumerate(connected_components):
    print(ii / len(connected_components))
    
    area = calculate_area(i, inp)
    c,p = calculate_permimeter(i, inp)
    sides = find_all_sides(i, p, inp)
    cs = find_connected_sides(sides)
    
    sums += len(cs)*area
    sums_p1 += area*c
    
    # for j in range(len(inp)):
    #     for k in range(len(inp[j])):
    #         if (j, k) in p:
    #             # print the number of sides for this point
    #             # since it can have 4 sides at most 0-4
    #             n = sum([1 for x in sides if x[0] == (k, j)])
    #             print(n, end='')
    #         elif (j, k) in i:
    #             print("0", end='')
    #         else:
    #             print(".", end='')
    #     print()
    # print()
      
print(sums_p1)  
print(sums)