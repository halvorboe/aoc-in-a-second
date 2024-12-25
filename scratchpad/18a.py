from heapq import heappop, heappush


with open("18.txt") as f:
    data = [tuple(int(n) for n in l.split(",")) for l in f]


nx, ny = 71, 71

g = dict()

print(data[:2881])
for x, y in data[:2881]:
    g[(x, y)] = True

for y in range(ny):
    for x in range(nx):
        if (x, y) in g:
            print("#", end="")
        else:
            print(".", end="")
    print()

start = (0, 0, 0)
end = (nx - 1, ny - 1)

print(nx, ny, start, end)

q = [start]

seen = set()

while q:
    d, x, y = heappop(q)
    if (x, y) in seen:
        continue
    seen.add((x, y))
    # print(x, y)
    if (x, y) == end:
        print(d)
        break
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        cx, cy = x + dx, y + dy
        # print(cx, cy)
        if cx < 0 or nx <= cx or cy < 0 or ny <= cy:
            continue
        if (cx, cy) in g:
            continue
        heappush(q, (d + 1, cx, cy))
