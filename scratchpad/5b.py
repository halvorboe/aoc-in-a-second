from collections import defaultdict, deque
from pprint import pprint
with open("5.txt") as f:
    rules, pages = f.read().split("\n\n")

rules = [tuple(int(n) for n in r.split("|")) for r in rules.splitlines()]
pages = [list(int(n) for n in r.split(",")) for r in pages.splitlines()]
print(rules, pages)



# mapping = dict((k, i) for i, k in enumerate(rules_order))

# pprint(graph)
# pprint(rules_order)


g = defaultdict(set)
for a, b in rules:
    g[b].add(a)
    g[a]

print(g)

s = 0

def calc(page):
    for i in range(1, len(page)):
        r_i = g[page[i]]
        for j in range(i):
            if page[j] not in r_i:
                return sort_page(page)
    return 0

def sort_page(page):
    print(g)
    print(page)
    p = set(page)
    s_g = {k: v.intersection(p) for k, v in g.items() if k in p}
    print("s_g", s_g)
    t = topo_sort(s_g)
    print("t",)
    return t[len(t) // 2]

def topo_sort(s_g):
    q = deque(k for k, v in s_g.items() if not v)

    order = []

    while q:
        n = q.popleft()
        order.append(n)
        for k, v in s_g.items():
            if n in v:
                v.remove(n)
                if not v:
                    q.append(k)

    return order


for page in pages:
    s += calc(page)

print(s)