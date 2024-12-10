from collections import deque, defaultdict


with open("10.txt") as f:
    g = [[int(n) for n in l.strip()] for l in f]

print(g)

n_r = len(g)
n_c = len(g[0])

for r in range(n_r):
    for c in range(n_c):
        print(g[r][c], end="")
    print()

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    s = 0
    for r in range(n_r):
        for c in range(n_c):
            if g[r][c] == 0:
                print("trailhead", r, c)
                s += score_trail(r, c)
    print(s)


def score_trail(sr, sc):
    q = deque()
    q.appendleft((sr, sc))

    score = 0
    seen = set()

    while q:
        r, c = q.popleft()
        if g[r][c] == 9:
            score += 1
            continue
        for dr, dc in D:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= n_r or nc < 0 or nc >= n_c:
                continue
            if g[nr][nc] == g[r][c] + 1:
                q.appendleft((nr, nc))
                print("trail", nr, nc)
    print(score)
    return score







main()