inp = [list(x.strip()) for x in open('in').readlines()]

global_start = None
global_end = None
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == 'S':
            global_start = (i, j)
        if inp[i][j] == 'E':
            global_end = (i, j)


# 0: up, 1: right, 2: down, 3: left
start_direction = 1

# run djikstra's algorithm

import heapq

def dijkstra_maze(inp, start, end, start_direction):
    rows, cols = len(inp), len(inp[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[[float('inf')] * 4 for _ in range(cols)] for _ in range(rows)]
    heap = []
    
    for dir_idx in range(4):
        if dir_idx == start_direction:
            initial_cost = 0
        else:
            initial_cost = 1000  
        heapq.heappush(heap, (initial_cost, start[0], start[1], dir_idx, [start]))
        visited[start[0]][start[1]][dir_idx] = initial_cost

    shortest_paths = []
    min_cost = float('inf')

    while heap:
        cost, x, y, dir_idx, path = heapq.heappop(heap)
        if cost > min_cost:
            continue
        if (x, y) == end:
            if cost < min_cost:
                min_cost = cost
                shortest_paths = [path]
            elif cost == min_cost:
                shortest_paths.append(path)
            continue
        for new_dir_idx, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and inp[nx][ny] != '#':
                new_cost = cost + 1
                if new_dir_idx != dir_idx:
                    new_cost += 1000
                if new_cost <= min_cost:
                    if new_cost < visited[nx][ny][new_dir_idx]:
                        visited[nx][ny][new_dir_idx] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny, new_dir_idx, path + [(nx, ny)]))
                    elif new_cost == visited[nx][ny][new_dir_idx]:
                        heapq.heappush(heap, (new_cost, nx, ny, new_dir_idx, path + [(nx, ny)]))
    return shortest_paths

paths = dijkstra_maze(inp, global_start, global_end, start_direction)

all_visited = set()
for path in paths:
    for cell in path:
        all_visited.add(cell)

print(len(all_visited))


