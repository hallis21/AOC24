

inp = [ x for x in open("in").read().split("\n\n")]





games = []
tokens_per_game = []
for game in inp:
    lines = [x.strip() for x in game.split("\n")]
    
    l1 = [int(x) for x in [(x.split("+")[1]) for x in lines[0].split(" A: ")[1].split(", ")]]
    l2 = [int(x) for x in [(x.split("+")[1]) for x in lines[1].split(" B: ")[1].split(", ")]]
    
    l3 = [int(x) for x in [(x.split("=")[1]) for x in lines[2].split("Prize: ")[1].split(", ")]]
    
    
    possible_bs = []
    possible_solution = []

    # find possible Bs that work with a
    for b in range(0, 101):
        bsum_x = l2[0] * b
        bsum_y = l2[1] * b
    
        rest_x = l3[0] - bsum_x
        rest_y = l3[1] - bsum_y
        
        if rest_x < 0 or rest_y < 0:
            continue
        
        # See if its divisible be l1, AND divide by the same number
        if rest_x % l1[0] == 0 and rest_y % l1[1] == 0 and rest_x // l1[0] == rest_y // l1[1]:
            x = rest_x // l1[0]
            if x > 100 or x < 0:
                continue
            possible_bs.append(b)
            possible_solution.append((x*3+ b))

    possible_solution_a = []
    # find possible As that work with b
    for a in range(0, 101):
        asum_x = l1[0] * a
        asum_y = l1[1] * a
    
        rest_x = l3[0] - asum_x
        rest_y = l3[1] - asum_y
        
        
        
        if rest_x < 0 or rest_y < 0:
            continue
        

        
        # See if its divisible be l1
        if rest_x % l2[0] == 0 and rest_y % l2[1] == 0 and rest_x // l2[0] == rest_y // l2[1]:
            x = rest_x // l2[0]
            if x > 100 or x < 0:
                continue
            possible_solution_a.append((a*3+x))
            
            
        
    if len(possible_bs) >= 1:
        tokens_per_game.append(min([min(possible_solution)]))
        
print()
print(sum(tokens_per_game))