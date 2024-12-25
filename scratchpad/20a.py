from collections import deque


with open("20.txt") as f:
    data = [l.strip() for l in f]

nr, nc = len(data), len(data[0])
g = set()
start = None
end = None

for r in range(nr):
    for c in range(nc):
        if data[r][c] == "#":
            g.add((r, c))
        elif data[r][c] == "S":
            start = (r, c)
        elif data[r][c] == "E":
            end = (r, c)


assert start and end

for r in range(nr):
    for c in range(nc):
        if (r, c) in g:
            print("#", end="")
        elif (r, c) == start:
            print("S", end="")
        elif (r, c) == end:
            print("E", end="")
        else:
            print(".", end="")
    print()

q = deque([(0, start[0], start[1])])
seen = dict()

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while q:
    d, r, c = q.pop()
    if (r, c) in seen:
        continue
    seen[(r, c)] = d
    if (r, c) == end:
        print(d)
        break
    print(r, c, d)
    for dr, dc in D:
        cr, cc = r + dr, c + dc
        if (cr, cc) not in g:
            q.appendleft((d + 1, cr, cc))
        # elif cheats > 0:
        #    heappush(q, (d + 1, cheats - 1, cr, cc))


assert nr * nc == len(seen) + len(g)

print(" " + "".join(str(n % 10) for n in range(nc)))
for r in range(nr):
    print(r % 10, end="")
    for c in range(nc):
        if (r, c) in g:
            print("#", end="")
        elif (r, c) == start:
            print("S", end="")
        elif (r, c) == end:
            print("E", end="")
        else:
            print(seen[(r, c)] % 10, end="")
    print()


C = [(a[0] + b[0], a[1] + b[1]) for a in D for b in D]
C = [c for c in C if c != (0, 0)]
C.sort()
# print(C)

cheats = []
for (sr, sc), sd in seen.items():
    for dr, dc in C:
        cr, cc = sr + dr, sc + dc
        if (cr, cc) in seen:
            gain = seen[(cr, cc)] - sd - 2
            if gain < 0:
                continue
            cheats.append(gain)
            print("cheat", sr, sc, gain)

cheats.sort()
from collections import Counter
counts = Counter(cheats)

print(counts)
print(sum(v for k, v in counts.items() if k >= 100))
