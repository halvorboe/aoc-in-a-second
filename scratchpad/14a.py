

with open("14.txt") as f:
    robots, velocities = zip(*(tuple(tuple(int(n) for n in v[2:].split(",")) for v in l.split()) for l in f))

print(robots, velocities)

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

for n in range(100):
    # print("=== Second", n, "===")
    # display(robots)
    robots = [((px + vx) % w, (py + vy) % h) for (px, py), (vx, vy) in zip(robots, velocities)]

display(robots)

mx = w // 2
my = h // 2

a, b, c, d = 0, 0, 0, 0
for x, y in robots:
    if x < mx and y < my:
        a += 1
    elif x < mx and y > my:
        b += 1
    elif x > mx and y < my:
        c += 1
    elif x > mx and y > my:
        d += 1

print(a * b * c * d)