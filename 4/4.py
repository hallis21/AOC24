def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
        
def diagonal_occurrences(diag_line, sub):
    string = "".join([x[0] for x in diag_line])
    return occurrences(string, sub)


inp = [x.strip().lower() for x in open("in").readlines()]

normal = sum([occurrences(line, "xmas")+occurrences(line, "samx") for line in inp])

# Transpose the matrix
transposed = list(map(list, zip(*inp)))
transposed = ["".join(x) for x in  transposed]

# Check for the same pattern in the transposed matrix
updown = sum([occurrences(line, "xmas")+occurrences(line, "samx") for line in transposed])


# Get diagonals
def get_diagonals(matrix):
    h = len(matrix)
    w = len(matrix[0])
    diags = []
    for i in range(h):
        diag = []
        for j in range(min(h-i, w)):
            
            # Coordinates of the current item (in the original matrix)
            item_coord = (i+j, j)
            
            diag.append((matrix[i+j][j], item_coord))
        diags.append(diag)
    for j in range(1, w):
        diag = []
        for i in range(min(h, w-j)):
            item_coord = (i, j+i)
            diag.append((matrix[i][j+i], item_coord))
        diags.append(diag)
    return diags



diag = sum([diagonal_occurrences(line, "xmas")+diagonal_occurrences(line, "samx") for line in get_diagonals(inp)])
diag2 = sum([diagonal_occurrences(line, "xmas")+diagonal_occurrences(line, "samx") for line in get_diagonals(inp[::-1])])


print(sum([normal, updown, diag, diag2]))


# Part 2

two_d = [list(x) for x in inp]



mas_coords = []

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if not(i+2 >= len(inp) or j+2 >= len(inp[0])):
            if inp[i][j] == "m" and inp[i+1][j+1] == "a" and inp[i+2][j+2] == "s":
                mas_coords.append((i+1, j+1))
            if inp[i][j] == "s" and inp[i+1][j+1] == "a" and inp[i+2][j+2] == "m":
                mas_coords.append((i+1, j+1))
        
        if not(i+2 >= len(inp) or j-2 < 0):
            if inp[i][j] == "m" and inp[i+1][j-1] == "a" and inp[i+2][j-2] == "s":
                mas_coords.append((i+1, j-1))
            if inp[i][j] == "s" and inp[i+1][j-1] == "a" and inp[i+2][j-2] == "m":
                mas_coords.append((i+1, j-1))
            

total = 0
for coord in set(mas_coords):
    if mas_coords.count(coord) > 1:
        total += 1
        
print(total)
            
            
# Print the original matrix with the MAS coordinates highlighted in red
# Green if the coordinate happens twice



