

from collections import defaultdict, deque


with open("24.txt") as f:
    values, gates = f.read().split("\n\n")

values = [(a, int(b)) for a,b in [l.split(": ") for l in values.splitlines()]]
gates = [l.split(" -> ") for l in gates.splitlines()]

g = defaultdict(list)
gop = dict()
gv = defaultdict(list)
gf = dict()

for i, t in gates:
    a, op, b = i.split()
    print(a, op, b, t)
    g[a].append(t)
    gop[t] = op
    g[b].append(t)

q = deque(values)

while q:
    c, v = q.popleft()
    print(c, v)
    for t in g[c]:
        gv[t].append(v)
        if len(gv[t]) == 2:
            op = gop[t]
            if op == "AND":
                gf[t] = gv[t][0] & gv[t][1]
            elif op == "OR":
                gf[t] = gv[t][0] | gv[t][1]
            elif op == "XOR":
                gf[t] = gv[t][0] ^ gv[t][1]
            else:
                raise ValueError("Unknown op")
            q.append((t, gf[t]))

print(g)
print(gv)
print(gop)
print(gf)

s = 0
for k, v in gf.items():
    if k.startswith("z"):
        s += v << int(k.lstrip("z"))

print(s)