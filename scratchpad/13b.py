import numpy as np

def parse(s):
    return tuple(int(v.strip()[2:]) for v in s.split(":")[1].split(","))

with open("13.txt") as f:
    parts = [tuple(parse(v) for v in p.split("\n")) for p in f.read().split("\n\n")]


# 1: a * ax + b * bx = px
# 2: a * ay + b * by = py


s = 0
score = np.array([3, 1])
for a, b, p in parts:
    print(a, b, p)
    ax, ay = a
    bx, by = b
    px, py = p
    px += 10000000000000
    py += 10000000000000
    l = np.array([[ax, bx], [ay, by]]).astype(np.float64)
    r = np.array([px, py]).astype(np.float64)
    solution = np.linalg.solve(l, r)

    if all(np.isclose(solution, np.round(solution), atol=0.0001, rtol=1e-30)):
        s += int(np.sum(np.round(solution) * score))


print(s)