# 1
print([sum([varr["is_good"](varr["inp"][rep]) for rep, _ in enumerate(varr["inp"])]) for varr in [{"inp":[[int(y) for y in x.strip().split(" ")] for x in open("in").readlines()],"is_good": lambda line: [(all(x < 0 for x in vars["diffs"]) or all(x > 0 for x in vars["diffs"])) and max([abs(x) for x in vars["diffs"]]) <= 3 and all(abs(x) > 0 for x in vars["diffs"]) for vars in [{"diffs": [line[y] - line[y+1] for y in range(len(line)) if y != len(line)-1]}]][0]}]][0])
# 2
print([sum([any([varr["is_good"]([x for x in varr["inp"][rep]][:i] + [x for x in varr["inp"][rep]][i+1:]) for i in range(len(varr["inp"][rep]))]) for rep, line in enumerate(varr["inp"])]) for varr in [{"inp":[[int(y) for y in x.strip().split(" ")] for x in open("in").readlines()],"is_good": lambda line: [(all(x < 0 for x in vars["diffs"]) or all(x > 0 for x in vars["diffs"])) and max([abs(x) for x in vars["diffs"]]) <= 3 and all(abs(x) > 0 for x in vars["diffs"]) for vars in [{"diffs": [line[y] - line[y+1] for y in range(len(line)) if y != len(line)-1]}]][0]}]][0])
            
    
            

