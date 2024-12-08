from collections import defaultdict


inp = [list(s.strip()) for s in open('in').readlines()]


antennas = defaultdict(lambda: list())

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] != '.':
            antennas[inp[y][x]].append((x, y))
        
antinodes = defaultdict(lambda: list())
extra_antinodes = defaultdict(lambda: list())

def distance(a, b):
    return (a[0] - b[0], a[1] - b[1])


for antenna_code in antennas:
    
    for i in range(len(antennas[antenna_code])):
        for j in range(i+1, len(antennas[antenna_code])):
            dist = distance(antennas[antenna_code][i], antennas[antenna_code][j])
            # 1
            antinodes[antenna_code].append((antennas[antenna_code][i][0]+dist[0], antennas[antenna_code][i][1]+dist[1]))
            antinodes[antenna_code].append((antennas[antenna_code][j][0]-dist[0], antennas[antenna_code][j][1]-dist[1]))
    
    
            extra_antinodes[antenna_code].append((antennas[antenna_code][i][0], antennas[antenna_code][i][1]))
            y1 = antennas[antenna_code][i][1] + dist[1]
            x1 = antennas[antenna_code][i][0] + dist[0]
            
            while 0 <= y1 < len(inp) and 0 <= x1 < len(inp[y1]):
                extra_antinodes[antenna_code].append((x1, y1))
                y1 += dist[1]
                x1 += dist[0]
                
            
            extra_antinodes[antenna_code].append((antennas[antenna_code][j][0], antennas[antenna_code][j][1]))
            y2 = antennas[antenna_code][j][1] - dist[1]
            x2 = antennas[antenna_code][j][0] - dist[0]
            
            while 0 <= y2 < len(inp) and 0 <= x2 < len(inp[y2]):
                extra_antinodes[antenna_code].append((x2, y2))
                y2 -= dist[1]
                x2 -= dist[0]
            
            
            
all_antinodes = set()
for antinode in extra_antinodes:
    for a in extra_antinodes[antinode]:
        # if outside the board do not add
        if a[0] < 0 or a[1] < 0 or a[0] >= len(inp[0]) or a[1] >= len(inp):
            continue
        all_antinodes.add(a)
# Print the board

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if (x, y) in all_antinodes:
            print('#', end='')
        else:
            print(inp[y][x], end='')
    print()
    
print(len(all_antinodes))