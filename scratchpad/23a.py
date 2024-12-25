
from collections import defaultdict


with open("23_test.txt") as f:
    data = [tuple(l.strip().split("-")) for l in f]

g = defaultdict(set)

for f, t in data:
    g[f].add(t)
    g[t].add(f)

g = dict(g)

groups = set()

for f, t in g.items():
    if f.startswith("t"):
        print(f, t)
        for it in t:
            st = g[it]
            ct = st.intersection(t)
            for jt in ct:
                items = f, it, jt
                groups.add("-".join(sorted(items)))
                # print("->", it, st, ct)

print(groups)
print(len(groups))

