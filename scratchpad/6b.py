from collections import defaultdict


with open('6.txt') as f:
    grid = [line.strip() for line in f]

n_r = len(grid)
n_c = len(grid[0]) if n_r > 0 else 0

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DM = {'^': 0, '>': 1, 'v': 2, '<': 3}

for l in grid:
    print(l)

start_r, start_c, start_d = None, None, None
for r in range(n_r):
    for c in range(n_c):
        if grid[r][c] in DM:
            start_r, start_c = r, c
            start_d = DM[grid[r][c]]
            break
    if start_r is not None:
        break

def is_free(r, c):
    if r < 0 or r >= n_r or c < 0 or c >= n_c:
        return True
    return grid[r][c] != '#'


def simulate(grid, o_r, o_c):
    d = start_d

    visited = defaultdict(set)
    visited[(start_r, start_c)].add(d)

    r, c = start_r, start_c

    while True:
        dr, dc = D[d]
        nr, nc = r + dr, c + dc
        if (not is_free(nr, nc)):
            d = (d + 1) % 4
        elif (nr, nc) == (o_r, o_c):
            d = (d + 1) % 4
        else:
            r, c = nr, nc
            if r < 0 or r >= n_r or c < 0 or c >= n_c:
                break
            if (r, c) in visited:
                if d in visited[(r, c)]:
                    print("loop")
                    return True
            visited[(r, c)].add(d)

    return False
    print(len(visited))
    for r in range(n_r):
        for c in range(n_c):
            if (r, c) == (o_r, o_c):
                print("O", end="")
            elif grid[r][c] == "." and (r, c) in visited:
                print("X", end="")
            else:
                print(grid[r][c], end="")
        print()

s = 0
for r in range(n_r):
    for c in range(n_c):
        if grid[r][c] == ".":
            if simulate(grid, r, c):
                s += 1
                print(s)
    else:
        continue
    break
