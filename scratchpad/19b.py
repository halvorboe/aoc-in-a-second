from dataclasses import dataclass
from typing import Dict

with open("19.txt") as f:
    towels, patterns = f.read().split("\n\n")

towels = [t.strip() for t in towels.strip().split(",")]
towels.sort()
# print(towels)
patterns = patterns.splitlines()
# print(patterns)

@dataclass
class Node:
    children: Dict[str, "Node"]
    value: int
    character: str

    def __repr__(self):
        return f"{self.character} -> {len(self.children)}"




start = Node(dict(), 0, "[START]")
end = Node(dict(), 2 ** 32, "[END]")

for pattern in towels:
    current_node = start
    # print(pattern)
    for i, c in enumerate(pattern):
        # print(i, c)
        if c in current_node.children:
            current_node = current_node.children[c]
        else:
            new_node = Node(dict(), i, c)
            current_node.children[c] = new_node
            current_node = new_node
    current_node.children["[END]"] = end

# print(start)

def print_node(node, indent=0):
    for k, v in node.children.items():
        print("-" * indent + "> " + k)
        print_node(v, indent + 2)

# print_node(start)

s = 0
for pattern in patterns:
    current_nodes = [(1, start)]
    for character in pattern:
        # print(current_nodes)
        new_nodes = []
        start_ways = 0
        for ways, current_node in current_nodes:
            if character in current_node.children:
                new_node = current_node.children[character]
                if "[END]" in new_node.children:
                    start_ways += ways
                new_nodes.append((ways, new_node))
        if start_ways > 0:
            new_nodes.append((start_ways, start))
        current_nodes = new_nodes

    # print(current_nodes)
    for ways, current_node in current_nodes:
        if "[END]" in current_node.children:
            # print("MATCH", pattern, ways)
            s += ways
    else:
        pass

        # print("NO MATCH", pattern)

print(s)
