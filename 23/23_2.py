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

def find_max_clique(nodes):
    def choose_pivot(candidates, excluded):
        # Choose pivot vertex that maximizes connections to candidates
        max_connections = -1
        pivot = None
        for v in candidates | excluded:
            connections = len(set(nodes[v]) & candidates)
            if connections > max_connections:
                max_connections = connections
                pivot = v
        return pivot

    def bron_kerbosch(candidates, current, excluded, max_clique):
        if not candidates and not excluded:
            if len(current) > len(max_clique[0]):
                max_clique[0] = current.copy()
            return
        
        pivot = choose_pivot(candidates, excluded)
        for v in candidates - set(nodes[pivot] if pivot else []):
            new_candidates = candidates & set(nodes[v])
            new_excluded = excluded & set(nodes[v])
            bron_kerbosch(new_candidates, current | {v}, new_excluded, max_clique)
            candidates.remove(v)
            excluded.add(v)

    all_vertices = set(nodes.keys())
    max_clique = [set()]  # Using list to allow modification in recursive function
    bron_kerbosch(all_vertices, set(), set(), max_clique)
    return max_clique[0]

def p1():
    max_clique = find_max_clique(nodes)
    print("Maximum clique size:", len(max_clique))
    print("Nodes in maximum clique:", ",".join(sorted(max_clique)))

p1()

