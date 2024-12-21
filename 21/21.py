inp = [list(x.strip()) for x in open("in").readlines()]



keypad_coords = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0), 
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    None: (3,0),
    '0': (3, 1),
    'A': (3, 2),
}

dir_chars = {
    (0, 1): '>',
    (0, -1): '<',
    (1, 0): 'v',
    (-1, 0): '^'
}

def get_paths(start, end):
    start_x, start_y = start
    end_x, end_y = end
    
    # If same x or y coordinate, only one straight path is possible
    if start_x == end_x:
        step = 1 if end_y >= start_y else -1
        return ([(start_x, y) for y in range(start_y, end_y + step, step)], None)
    if start_y == end_y:
        step = 1 if end_x >= start_x else -1
        return ([(x, start_y) for x in range(start_x, end_x + step, step)], None)
    
    # Two possible paths with one turn:
    # 1. Move horizontally first, then vertically
    path1 = [(start_x, y) for y in range(min(start_y, end_y), max(start_y, end_y) + 1)]
    path1 = path1 if start_y < end_y else path1[::-1]
    vert1 = [(x, end_y) for x in range(min(start_x, end_x), max(start_x, end_x) + 1)]
    path1 = path1[:-1] + (vert1 if start_x < end_x else vert1[::-1])
    
    # 2. Move vertically first, then horizontally
    path2 = [(x, start_y) for x in range(min(start_x, end_x), max(start_x, end_x) + 1)]
    path2 = path2 if start_x < end_x else path2[::-1]
    horz2 = [(end_x, y) for y in range(min(start_y, end_y), max(start_y, end_y) + 1)]
    path2 = path2[:-1] + (horz2 if start_y < end_y else horz2[::-1])
    
    return (path1, path2)

def pick_legal_path(paths, reversed_keymap):
    path1, path2 = paths
    if path2 is None:
        return path1, None
    if path1 is None:
        return None, path2
    # keymape_entries = keymap.values()
    if any(reversed_keymap.get(x) is None for x in path1):
        return None, path2
    if any(reversed_keymap.get(x) is None for x in path2):
        return path1, None
    return path1, path2
    
def reverse_dict(d):
    return {v: k for k, v in d.items()}
    
    
def convert_to_directions(path):
    directions = []
    for i in range(1, len(path)):
        x1, y1 = path[i-1]
        x2, y2 = path[i]
        directions.append(dir_chars[(x2 - x1, y2 - y1)])
    return directions

dirpad_coords = {
    None: (0,0),
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

def get_all_paths_recursive(code, cur_coord=None, path_so_far=None, index=0):
    if cur_coord is None:
        cur_coord = keypad_coords['A']
    if path_so_far is None:
        path_so_far = []
    
    if index >= len(code):
        return [path_so_far]
    
    next_coords = keypad_coords.get(code[index])
    paths = get_paths(cur_coord, next_coords)
    path1, path2 = pick_legal_path(paths, reverse_dict(keypad_coords))
    
    all_paths = []
    for valid_path in [path1, path2]:
        if valid_path is not None:
            dirs = convert_to_directions(valid_path)
            new_path = path_so_far + dirs + ['A']
            all_paths.extend(get_all_paths_recursive(code, next_coords, new_path, index + 1))
    
    return all_paths

combinations = []
for code in inp[:]:
    paths = get_all_paths_recursive(code)
    min_len = min(len(x) for x in paths)
    paths = [x for x in paths if len(x) == min_len]
    combinations.append(paths)
    
    

def get_all_dirpad_recursive(combination, cur_coord=None, path_so_far=None, index=0):
    if cur_coord is None:
        cur_coord = dirpad_coords['A']
    if path_so_far is None:
        path_so_far = []
    
    if index >= len(combination):
        return [path_so_far]
    
    next_coords = dirpad_coords.get(combination[index])
    paths = get_paths(cur_coord, next_coords)
    path1, path2 = pick_legal_path(paths, reverse_dict(dirpad_coords))
    
    all_paths = []
    for valid_path in [path1, path2]:
        if valid_path is not None:
            dirs = convert_to_directions(valid_path)
            new_path = path_so_far + dirs + ['A']
            all_paths.extend(get_all_dirpad_recursive(combination, next_coords, new_path, index + 1))
    
    
    min_len = min(len(x) for x in all_paths)
    all_paths = [x for x in all_paths if len(x) == min_len]
    
    return all_paths

robotception = 2

score = 0
for i, code_paths in enumerate(combinations[:1]):
    all_path_combos = []
    for path in code_paths:
        all_combos = get_all_dirpad_recursive(path)
        for ii in range(robotception-1):
            print(ii)
            next_combos = []
            for combo in all_combos:
                new_paths = get_all_dirpad_recursive(combo)
                min_len = min(len(x) for x in new_paths)
                new_paths = [x for x in new_paths if len(x) == min_len]
                next_combos.extend(new_paths)
            all_combos = next_combos
            
        min_len = min(len(x) for x in all_combos)
        all_combos = [x for x in all_combos if len(x) == min_len]
        
        all_path_combos.extend(all_combos)
        
        
        
    min_len = min(len(x) for x in all_path_combos)
    print(min_len, int("".join(inp[i][:-1])))
    score += min_len * int("".join(inp[i][:-1]))

        

    # for path in code_paths:
    #     cur_combo = path
    #     for _ in range(robotception):  # -1 because we're already doing one level
    #         next_paths = []
    #         for combo in (cur_combo if isinstance(cur_combo, list) else [cur_combo]):
    #             next_paths.extend(get_all_dirpad_recursive(combo))
    #         cur_combo = next_paths
        
    #     # Get the shortest path
    #     shortest_path = min(cur_combo, key=len)
    #     score += len(shortest_path) * int("".join(inp[i][:-1]))

print(score)