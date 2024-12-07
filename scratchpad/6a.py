
with open('6.txt') as f:
    grid = [line.strip() for line in f]

n_r = len(grid)
n_c = len(grid[0]) if n_r > 0 else 0

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DM = {'^': 0, '>': 1, 'v': 2, '<': 3}

for l in grid:
    print(l)

start_r, start_c, d = None, None, None
for r in range(n_r):
    for c in range(n_c):
        if grid[r][c] in DM:
            start_r, start_c = r, c
            d = DM[grid[r][c]]
            break
    if start_r is not None:
        break

visited = set()
visited.add((start_r, start_c))

r, c = start_r, start_c

while True:
    dr, dc = D[d]
    nr, nc = r + dr, c + dc
    if nr < 0 or nr >= n_r or nc < 0 or nc >= n_c:
        break
    if not is_free(nr, nc):
        d = (d + 1) % 4
    else:
        r, c = nr, nc
        if r < 0 or r >= n_r or c < 0 or c >= n_c:
            break
        visited.add((r, c))

print(len(visited))
