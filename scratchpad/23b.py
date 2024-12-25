from collections import defaultdict
from itertools import combinations


with open("23.txt") as f:
    data = [tuple(l.strip().split("-")) for l in f]

g = defaultdict(set)

for f, t in data:
    g[f].add(t)
    g[t].add(f)

g = dict(g)

largest_seen = 0
best = None

for f, t in g.items():
    for n in range(largest_seen, len(t) + 1):
        for combo in combinations(t.union({f}), n):
            s = set(combo)
            match = True
            for c in s:
                if  len(s.intersection(g[c]))  < len(s) - 1:
                    match = False
                    break
            if match:
                largest_seen = len(s)
                best = s
                # print(match, s)

print(largest_seen)
print(",".join(sorted(best)))