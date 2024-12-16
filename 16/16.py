import sys
import heapq

sys.setrecursionlimit(10000)

inp = [list(x.strip()) for x in open('in').readlines()]

global_start = None
global_end = None
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == 'S':
            global_start = (i, j)
        if inp[i][j] == 'E':
            global_end = (i, j)

def heuristic(pos, end, curr_dir):
    # Manhattan distance for minimum steps
    dx = abs(pos[0] - end[0])
    dy = abs(pos[1] - end[1])
    min_steps = dx + dy
    
    # Minimum turns needed
    min_turns = 0
    if dx > 0 and dy > 0:
        min_turns = 1
    
    return min_steps + min_turns * 1000

def a_star():
    start = global_start
    end = global_end
    # (priority, pos, turns, steps, current_direction)
    pq = [(0, start, 0, 0, 1)]
    best_scores = {}
    min_score = float('inf')

    while pq:
        priority, (x, y), turns, steps, curr_dir = heapq.heappop(pq)
        state = (x, y, curr_dir)
        current_score = steps + turns * 1000
        
        if state in best_scores and current_score >= best_scores[state]:
            continue
        best_scores[state] = current_score

        if (x, y) == end:
            min_score = min(min_score, current_score)
            continue

        for i, j, new_dir in [(0, 1, 1), (0, -1, 3), (1, 0, 2), (-1, 0, 0)]:
            new_x, new_y = x + i, y + j
            if 0 <= new_x < len(inp) and 0 <= new_y < len(inp[0]) and inp[new_x][new_y] != '#':
                new_turns = turns
                new_steps = steps + 1
                if curr_dir is not None and new_dir != curr_dir:
                    new_turns += 1
                new_score = new_steps + new_turns * 1000
                new_state = ((new_x, new_y), new_dir)
                if new_state not in best_scores or new_score < best_scores[new_state]:
                    priority = new_score + heuristic((new_x, new_y), end, new_dir)
                    heapq.heappush(pq, (priority, (new_x, new_y), new_turns, new_steps, new_dir))

    print(min_score)

a_star()