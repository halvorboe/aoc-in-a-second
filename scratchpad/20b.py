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


max_d = max(seen.values())
cheats = dict()
for (sr, sc), sd in seen.items():
    for er in range(max(0, sr - 20), min(nr, sr + 21)):
        for ec in range(max(0, sc - 20), min(nc, sc + 21)):
            d = abs(sr - er) + abs(sc - ec)
            if d > 20 or (er, ec) not in seen:
                continue
            gain = seen[(er, ec)] - sd - d
            if gain > 0:
                cheats[(sr, sc, er, ec)] = gain


# print(list((k, v) for k, v in cheats.items() if v >= 73))

from collections import Counter
cheat_values = list(cheats.values())
cheat_values.sort()
counts = Counter(cheat_values)

# print(counts)
print(sum(v for k, v in counts.items() if k >= 100))
