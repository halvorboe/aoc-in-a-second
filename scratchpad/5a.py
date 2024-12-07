from collections import defaultdict, deque
from pprint import pprint
with open("5.txt") as f:
    rules, pages = f.read().split("\n\n")

rules = [tuple(int(n) for n in r.split("|")) for r in rules.splitlines()]
pages = [list(int(n) for n in r.split(",")) for r in pages.splitlines()]
print(rules, pages)
"""
def topo_sort(rules):
    g = defaultdict(list)
    for a, b in rules:
        g[b].append(a)
        g[a]

    graph = dict((k, list(v)) for k, v in g.items())
    q = deque(k for k, v in g.items() if not v)

    order = []

    while q:
        n = q.popleft()
        order.append(n)
        for k, v in g.items():
            if n in v:
                v.remove(n)
                if not v:
                    q.append(k)

    return order, graph

rules_order, graph = topo_sort(rules)
"""

# mapping = dict((k, i) for i, k in enumerate(rules_order))

# pprint(graph)
# pprint(rules_order)


g = defaultdict(set)
for a, b in rules:
    g[b].add(a)

print(g)

s = 0

def calc(page):
    for i in range(1, len(page)):
        r_i = g[page[i]]
        for j in range(i):
            print(i, j)
            print(page[i], page[j], r_i)
            if page[j] not in r_i:
                print("MATCH")
                return 0
    return page[len(page)//2]


for page in pages:
    s += calc(page)
print(s)