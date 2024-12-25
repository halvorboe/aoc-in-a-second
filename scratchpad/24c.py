
def parse_input(input_file):
    """
    Parses the input file into initial wire values and gate definitions.
    """
    wire_values = {}
    gates = []

    with open(input_file, "r") as f:
        for line in map(str.strip, f):
            if not line:
                continue

            if ":" in line:  # Initial wire values
                wire, value = map(str.strip, line.split(":"))
                wire_values[wire] = int(value)
            elif "->" in line:  # Gate definitions
                inputs, output = map(str.strip, line.split("->"))

                for op in ["AND", "XOR", "OR"]:
                    if op in inputs:
                        in1, in2 = map(str.strip, inputs.split(op))
                        gates.append({"a": in1, "op": op, "b": in2, "output": output})
                        break
                else:
                    raise ValueError(f"Unknown gate format: {line}")

    return wire_values, gates

def find_gate(gates, a, b=None, op=None):
    """
    Finds a gate matching the given inputs and operation.
    If `b` is None, it finds a gate with only one input.
    """
    return next(
        (
            g for g in gates
            if g["op"] == op and (
                (g["a"] == a and g["b"] == b) or
                (g["a"] == b and g["b"] == a) if b else g["a"] == a or g["b"] == a
            )
        ),
        {"output": "!!!"}
    )

def apply_swaps(gates, swaps):
    """
    Applies swaps to the gate outputs based on the given swap mappings.
    """
    swap_dict = {swaps[i]: swaps[i + 1] for i in range(0, len(swaps), 2)}
    swap_dict.update({v: k for k, v in swap_dict.items()})

    for gate in gates:
        if gate["output"] in swap_dict:
            gate["output"] = swap_dict[gate["output"]]

def visualize_circuit_full_adder(wire_values, gates, swaps):
    """
    Creates an ASCII visualization of the full adder circuit for all bits.
    """
    visualization = []
    input_bits = sorted(
        (wire for wire in wire_values if wire.startswith("x")),
        key=lambda w: int(w[1:])
    )
    num_bits = len(input_bits)

    apply_swaps(gates, swaps)
    carrier_bit = find_gate(gates, "x00", "y00", "AND")["output"]

    for i in range(1, num_bits):
        x, y, z = (f"x{i:02d}", f"y{i:02d}", f"z{i:02d}")

        try:
            # Find gates for current bit
            xor1 = find_gate(gates, x, y, "XOR")
            and1 = find_gate(gates, x, y, "AND")
            xor2 = find_gate(gates, xor1["output"], carrier_bit, "XOR")
            and2 = find_gate(gates, xor1["output"], carrier_bit, "AND")
            or_gate = find_gate(gates, and1["output"], and2["output"], "OR")

            # Update carrier bit
            carrier_bit = or_gate["output"]

            # Visualization for current bit
            visualization.append(f"Bit {i:02d} Visualization:")
            visualization.append(f"{x} --| [XOR] --> {xor1['output']} --| [XOR] --> {xor2['output']} ({z})")
            visualization.append(f"{y} --|                |              |")
            visualization.append(f"                        | [AND] --> {and1['output']}")
            visualization.append(f"Carrier: {carrier_bit}")
            visualization.append("")

        except Exception as e:
            visualization.append(f"Error processing bit {i}: {e}")

    print("\n".join(visualization))

def process_circuit(input_file):
    """
    Processes the circuit and visualizes the full adder for all bits.
    """
    wire_values, gates = parse_input(input_file)
    swaps = ["kth", "z12", "gsd", "z26", "tbt", "z32", "qnf", "vpm"]

    print("Circuit Visualization:")
    visualize_circuit_full_adder(wire_values, gates, swaps)
    return swaps

if __name__ == "__main__":
    input_file = "24.txt"
    swaps = process_circuit(input_file)
    print(",".join(sorted(swaps)))
