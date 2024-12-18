import heapq


def part1(N):
    inp = [(*tuple(map(int, x.strip().split(","))), i)for i, x in enumerate(open("in").readlines())]
    
    grid_x = 70
    grid_y = 70
    
    grid = [[None for _ in range(grid_x+1)] for _ in range(grid_y+1)]


    # place the inp (x,y, id) on the grid
    for x, y, id in inp[:N]:
        grid[y][x] = id
        

    def print_grid(grid):
        for row in grid:
            for cell in row:
                if cell is None:
                    print(" .", end=" ")
                else:
                    print(f"{cell:2}", end=" ")
            print()
        print()
        
        
        
        
    # Move through the maze using A* algorithm
    # only find the shortest path

    # find the shortest path from 0,0 to grid_x, grid_y using A* algorithm

    def dijkstra(grid, start, end):
        heap = [(0, start)]
        distances = {start: 0}
        visited = set()

        while heap:
            cost, current = heapq.heappop(heap)
            if current == end:
                return cost
            if current in visited:
                continue
            visited.add(current)
            x, y = current
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= grid_x and 0 <= ny <= grid_y:
                    if grid[ny][nx] is None and (nx, ny) not in visited:
                        next_cost = cost + 1
                        if distances.get((nx, ny), float('inf')) > next_cost:
                            distances[(nx, ny)] = next_cost
                            heapq.heappush(heap, (next_cost, (nx, ny)))
        return None  # No path found

    start = (0, 0)
    end = (grid_x, grid_y)
    distance = dijkstra(grid, start, end)
    
    return distance


print(part1(1024))

max_steps = 3450
inp = [(*tuple(map(int, x.strip().split(","))), i)for i, x in enumerate(open("in").readlines())]
for N in range(12, max_steps):
    if part1(N) is None:
        print(inp[N-1])
        break
