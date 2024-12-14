
def parse(s):
    return tuple(int(v.strip()[2:]) for v in s.split(":")[1].split(","))

with open("13.txt") as f:
    parts = [tuple(parse(v) for v in p.split("\n")) for p in f.read().split("\n\n")]

s = 0
for a, b, p in parts:
    print(a, b, p)
    ax, ay = a
    bx, by = b
    px, py = p
    best = (-1, -1)
    n = 0
    for n in range(101):
        x, y = n * bx, n * by
        if x > px or y > py:
            break
        rx, ry = px - x, py - y
        if rx % ax == 0 and ry % ay == 0 and rx // ax == ry // ay:
            print(n, x, y, rx, ry)
            best = (rx // ax, n)
    print(best)
    ba, bb = best
    if ba != -1 and bb != -1:
        assert ax * ba + bx * bb == px
        assert ay * ba + by * bb == py
        s += ba * 3 + bb * 1

print(s)