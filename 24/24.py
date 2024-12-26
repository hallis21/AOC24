from collections import defaultdict


inp = open("in").read().split("\n\n")


ini = [x.split(": ") for x in inp[0].split("\n")]

vals = defaultdict(lambda: None)

for x in ini:
    vals[x[0]] = bool(int(x[1]))
    

    

# (inp1, inp2, opr, out)
unchecked_gates = []

for x in inp[1].split("\n"):
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
    
    
    
out_vals = sorted([x for x in vals.keys() if "z" in x])

# Make a binary number from the output values, the 
out = 0
for i, x in enumerate(out_vals):
    out += int(vals[x]) << i


print(out)