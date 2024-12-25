from collections import defaultdict, deque


with open("24.txt") as f:
    values, gates = f.read().split("\n\n")

values = dict((a, int(b)) for a,b in [l.split(": ") for l in values.splitlines()])
gates = {k: v for v, k in [l.split(" -> ") for l in gates.splitlines()]}


def generate_graphviz_spec(values, gates):
    """
    Generates a Graphviz spec for the logic circuit.
    """
    graphviz = ["digraph LogicCircuit {"]
    graphviz.append("    rankdir=UD;")  # Set left-to-right layout
    graphviz.append("    node [shape=box];")  # Use box shapes for nodes

    # Add nodes for wire values
    for wire, value in values.items():
        graphviz.append(f"    {wire} [label=\"{wire}: {value}\", shape=circle];")

    # Add nodes and connections for gates
    for output, inputs in gates.items():
        inputs_split = inputs.split()
        if "AND" in inputs_split:
            op = "AND"
            in1, in2 = inputs_split[0], inputs_split[2]
        elif "OR" in inputs_split:
            op = "OR"
            in1, in2 = inputs_split[0], inputs_split[2]
        elif "XOR" in inputs_split:
            op = "XOR"
            in1, in2 = inputs_split[0], inputs_split[2]
        else:
            raise ValueError(f"Unknown gate operation: {inputs}")

        # Add gate node
        gate_label = f"{output}"
        if "z" in gate_label:
            graphviz.append(f"    {gate_label} [label=\"{output} = {op}\", shape=square];")
        else:
            graphviz.append(f"    {gate_label} [label=\"{output} = {op}\", shape=diamond];")

        # Connect inputs to gate
        graphviz.append(f"    {in1} -> {gate_label};")
        graphviz.append(f"    {in2} -> {gate_label};")

    graphviz.append("}")
    return "\n".join(graphviz)



# Generate Graphviz Spec
graphviz_spec_before = generate_graphviz_spec(values, gates)
with open("before.dot", "w+") as f:
    f.write(graphviz_spec_before)



swaps = [("kth", "z12"), ("gsd", "z26"), ("z32", "tbt"), ("qnf", "vpm")]

for sf, st in swaps:
    gates[sf], gates[st] = gates[st], gates[sf]

graphviz_spec_after = generate_graphviz_spec(values, gates)
with open("after.dot", "w+") as f:
    f.write(graphviz_spec_after)

