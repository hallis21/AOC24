inp = [ x for x in open("in").read().split("\n\n")]





games = []
all_games = []
tokens_per_game = []
for game in inp:
    lines = [x.strip() for x in game.split("\n")]
    
    l1 = [int(x) for x in [(x.split("+")[1]) for x in lines[0].split(" A: ")[1].split(", ")]]
    l2 = [int(x) for x in [(x.split("+")[1]) for x in lines[1].split(" B: ")[1].split(", ")]]
    
    l3 = [int(x) for x in [(x.split("=")[1]) for x in lines[2].split("Prize: ")[1].split(", ")]]
    l3_2 = [x + 10000000000000 for x in l3]
    all_games.append([l1, l2, l3_2])



# Output all_games as a golang int64 array (a game should be structured as [l1, l2, l3])

print("package main")
print("var games = [][][]int64{")
for game in all_games:
    print("{")
    print("{", end="")
    print(*game[0], sep=", ", end="")
    print("},")
    print("{", end="")
    print(*game[1], sep=", ", end="")
    print("},")
    print("{", end="")
    print(*game[2], sep=", ", end="")
    print("},")
    print("},")
print("}")




