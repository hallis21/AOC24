def gate_symbol(gate_type):
    if gate_type == "AND":
        return "(&)"
    elif gate_type == "OR":
        return "(≥1)"
    elif gate_type == "XOR":
        return "(=1)"
    return ""

# Read input file
with open("in") as f:
    inp = f.read().split("\n\n")

# Create mermaid markdown content
mermaid_content = ["graph TB"]  # Changed from LR to BT for bottom-to-top direction

# Add input nodes
init_values = [x.split(": ") for x in inp[0].split("\n")]
for node, value in init_values:
    mermaid_content.append(f"    {node}[/{node}/]")

# Add gate connections
gates = inp[1].split("\n")
for gate in gates:
    if not gate:  # Skip empty lines
        continue
    parts = gate.split(" ")
    input1, op, input2, arrow, output = parts
    
    # Create gate node and connections
    gate_id = f"gate_{input1}_{op}_{input2}"
    mermaid_content.append(f"    {gate_id}[{gate_symbol(op)}]")
    mermaid_content.append(f"    {input1} --> {gate_id}")
    mermaid_content.append(f"    {input2} --> {gate_id}")
    mermaid_content.append(f"    {gate_id} --> {output}")
    mermaid_content.append(f"    {output}[[{output}]]")


# Write to output file
with open('circuit.mmd', 'w') as f:
    f.write('\n'.join(mermaid_content))
