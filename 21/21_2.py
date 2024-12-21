from functools import lru_cache

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

@lru_cache(maxsize=None)
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

def pick_legal_path(paths, reversed_keymap, cache=None):
    if cache is None:
        cache = {}
    path1, path2 = paths
        
    key = (tuple(path1) if path1 is not None else None, tuple(path2) if path2 is not None else None)
    if key in cache:
        return cache[key]
    
    if path2 is None:
        cache[key] = path1, None
        return path1, None
    if path1 is None:
        cache[key] = None, path2
        return None, path2
    # keymape_entries = keymap.values()
    if any(reversed_keymap.get(x) is None for x in path1):
        cache[key] = None, path2
        return None, path2
    if any(reversed_keymap.get(x) is None for x in path2):
        cache[key] = path1, None
        return path1, None
    
    cache[key] = path1, path2
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

@lru_cache(maxsize=None)
def get_all_paths_recursive(code, cur_coord, index=0):
    if index >= len(code):
        return [()]
    
    next_coords = keypad_coords.get(code[index])
    paths = get_paths(cur_coord, next_coords)
    path1, path2 = pick_legal_path(paths, reverse_dict(keypad_coords))
    
    all_paths = []
    for valid_path in [path1, path2]:
        if valid_path is not None:
            dirs = convert_to_directions(valid_path)
            for sub_path in get_all_paths_recursive(code, next_coords, index + 1):
                all_paths.append(tuple(dirs + ['A'] + list(sub_path)))
    
    return tuple(all_paths)

def get_all_dirpad_recursive(combination, cur_coord, cache=None):
    if cache is None:
        cache = {}
    
    cache_key = (combination, cur_coord)
    if cache_key in cache:
        return cache[cache_key]
    
    if not combination:  # Empty combination
        return [()]
    
    next_coords = dirpad_coords.get(combination[0])
    paths = get_paths(cur_coord, next_coords)
    path1, path2 = pick_legal_path(paths, reverse_dict(dirpad_coords))
    
    all_paths = []
    for valid_path in [path1, path2]:
        if valid_path is not None:
            dirs = convert_to_directions(valid_path)
            for sub_path in get_all_dirpad_recursive(combination[1:], next_coords, cache):
                all_paths.append(tuple(dirs + ['A'] + list(sub_path)))
    
    min_len = min(len(x) for x in all_paths)
    all_paths = tuple(x for x in all_paths if len(x) == min_len)
    
    cache[cache_key] = all_paths
    return all_paths

combinations = []
for code in inp[:]:
    get_all_paths_recursive.cache_clear()  # Clear cache for each new code
    paths = get_all_paths_recursive(tuple(code), keypad_coords['A'])
    min_len = min(len(x) for x in paths)
    paths = [list(x) for x in paths if len(x) == min_len]
    combinations.append(paths)
    


@lru_cache(maxsize=None)
def get_sequence_dirpad(key, prev_key, ception=0):
    if ception == 0:
        return 1  # Base case
    
    cur_coord = dirpad_coords[prev_key]
    next_coords = dirpad_coords[key]
    
    path1, path2 = pick_legal_path(get_paths(cur_coord, next_coords), reverse_dict(dirpad_coords))
    min_total = float('inf')
    
    for path in [path1, path2]:
        if path is not None:
            comb = convert_to_directions(path) + ['A']
            total_len = 0
            prev = "A"
            for next_key in comb:
                total_len += get_sequence_dirpad(next_key, prev, ception - 1)
                prev = next_key
            min_total = min(min_total, total_len)
    
    return min_total

score = 0
for ii, combination in enumerate(combinations):
    path_lengths = []

    for comb in combination:
        length = 0
        prev_key = "A"
        for key in comb:
            length += get_sequence_dirpad(key, prev_key, 25)
            prev_key = key
        path_lengths.append(length)
    min_len = min(path_lengths)
    score += min_len * int("".join(inp[ii][:-1]))

print(score)

