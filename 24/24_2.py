from collections import defaultdict


inp = open("in").read().split("\n\n")


ini = [x.split(": ") for x in inp[0].split("\n")]

vals = defaultdict(lambda: None)

import random
for x in ini:
    vals[x[0]] = bool(random.randint(0, 1))
    
xval = sorted([x for x in vals.keys() if "x" in x])

xin = 0
for i, x in enumerate(xval):
    xin += int(vals[x]) << i
    
yval = sorted([x for x in vals.keys() if "y" in x])

yin = 0
for i, x in enumerate(yval):
    yin += int(vals[x]) << i
    
    
# Test use &, real is +
target = xin + yin 

target_vals = {}

# For each bit in the target, add a zXX value to the target_vals dict
# least significant bit is z0
bits = 0
while target:
    target_vals[f"z{bits:02}"] = target & 1
    target >>= 1
    bits += 1
target_vals[f"z{bits:02}"] = 0
    


def run_gates(gates, init_vals):
    
    vals = defaultdict(lambda: None)
    
    for x in init_vals.keys():
        vals[x] = init_vals[x]

    # (inp1, inp2, opr, out)
    unchecked_gates = []

    for x in gates:
        x = x.split(" ")
        unchecked_gates.append((x[0], x[2], x[1], x[-1]))
        
    i = 0
    while unchecked_gates:
        if i >= len(unchecked_gates):
            i = 0
        
        gate = unchecked_gates[i]
        
        if vals[gate[0]] is not None and vals[gate[1]] is not None:
            if gate[2] == "AND":
                    vals[gate[3]] = vals[gate[0]] & vals[gate[1]]
            elif gate[2] == "OR":
                    vals[gate[3]] = vals[gate[0]] | vals[gate[1]]
            elif gate[2] == "XOR":
                    vals[gate[3]] = vals[gate[0]] ^ vals[gate[1]]
            unchecked_gates.pop(i)
                
        i += 1
    return vals



def find_wrong_vals(gates, init_vals, target_vals):
    new_vals = run_gates(gates, init_vals)
    out_vals = sorted([x for x in new_vals.keys() if "z" in x])
    
    out = 0
    for i, x in enumerate(out_vals):
        out += new_vals[x] << i
        
    print(out)
    print(yin + xin)
    
    return [x for x in out_vals if new_vals[x] != target_vals[x]]
# new_vals = run_gates(inp[1].split("\n"), vals)
    
    

print(find_wrong_vals(inp[1].split("\n"), vals, target_vals))



swapped = ["z07", "swt",
"z13", "pqc",
"rjm", "wsv",
"z31", "bgs"]

print(",".join(sorted(swapped)))

