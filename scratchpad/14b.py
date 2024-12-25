
with open("14.txt") as f:
    robots, velocities = zip(*(tuple(tuple(int(n) for n in v[2:].split(",")) for v in l.split()) for l in f))

# print(robots, velocities)

# w, h = 11, 7
w, h = 101, 103

def display(r):
    for y in range(h):
        for x in range(w):
            count = sum(1 for px, py in r if x == px and y == py)
            if count == 0:
                print(".", end='')
            else:
                print(count, end='')
        print()

def groups(r):
    s = 0
    ms = 0
    prev = (0, 0)
    for x, y in sorted(r, key=lambda t: (t[1], t[0])):
        if prev and prev == (x - 1, y):
            s += 1
        else:
            ms = max(s, ms)
            s = 1
        prev = (x, y)
        # print(x, y)
    # print(ms)
    return ms


for n in range(250000):
    # print("=== Second", n, "===")
    # display(robots)
    robots = [((px + vx) % w, (py + vy) % h) for (px, py), (vx, vy) in zip(robots, velocities)]
    ms =  groups(robots)
    if ms > 10:
        for _ in range(10):
            print()
        print("===", n + 1, "===")
        display(robots)
        break




