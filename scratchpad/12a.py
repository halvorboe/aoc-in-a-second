
with open("12.txt") as f:
    grid = [list(l.strip()) for l in f]

n_r = len(grid)
n_c = len(grid[0])



def flood():
    score = 0
    seen = set()
    for r in range(n_r):
        for c in range(n_c):
            if (r, c) in seen:
                continue
            p, a = compute_size(r, c, grid[r][c], seen)
            # print(r, c, grid[r][c], p, a, p * a)
            score += p * a
    print(score)

def compute_size(r, c, t, seen):
    seen.add((r, c))
    s = 0
    a = 1
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n_r or nc < 0 or nc >= n_c or grid[nr][nc] != t:
            # print("perimiter", nr, nc)
            s += 1
        elif (nr, nc) not in seen:
            # print("found", nr, nc)
            c_s, c_a = compute_size(nr, nc, t, seen)
            s += c_s
            a += c_a
        else:
            # print("skipped", nr, nc)
            pass
    # print("-> ", r, c, t, s)
    return (s, a)

# print(grid)
flood()