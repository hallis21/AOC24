from collections import defaultdict


inp = [x.strip().split("-") for x in open('in').readlines()]

nodes = defaultdict(list)

for node in inp:
    nodes[node[0]].append(node[1])
    nodes[node[1]].append(node[0])
    
def is_clique(nodes, group):
    for node in group:
        for other in group:
            if node != other and other not in nodes[node]:
                return False
    return True

def find_cliques(nodes, start, size=3):
    cliques = set()
    current_clique = {start}
    
    def extend_clique(current):
        if len(current) == size:
            cliques.add(tuple(sorted(current)))
            return
        
        candidates = set(nodes[start])
        for node in current:
            candidates &= set(nodes[node])
        
        for candidate in candidates - current:
            if is_clique(nodes, current | {candidate}):
                current.add(candidate)
                extend_clique(current)
                current.remove(candidate)
    
    extend_clique(current_clique)
    return cliques

def p1():
    all_cliques = set()
    for ii, node in enumerate(nodes):
        print(ii, node)
        all_cliques.update(find_cliques(nodes, node))
    
    all_cliques = [x for x in all_cliques if len(x) == 3]
    
    all_cliques = sorted(all_cliques, key=lambda x: x[0])
    
    all_cliques = [x for x in all_cliques if any(y.startswith("t") for y in x)]
    
    print(len(all_cliques))

p1()

