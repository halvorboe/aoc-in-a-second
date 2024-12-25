from collections import defaultdict, deque
from heapq import heappop, heappush

with open("16.txt") as f:
    grid = [l.strip() for l in f]

nr = len(grid)
nc = len(grid[0])



start = None
end = None

for r in range(nr):
    for c in range(nc):
        if grid[r][c] == "S":
            start = (0, r, c, ">", -1, -1, "S")
        if grid[r][c] == "E":
            end = (r, c)
        print(grid[r][c], end="")
    print()


assert start
assert end
print(start, end)

q = [start]

seen = dict()
prev = defaultdict(set)

D = {">": "^v", "<": "^v", "^": "<>", "v": "<>"}
M = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

best_score = -1

while q:
    score, r, c, d, pr, pc, pd = heappop(q)
    # print(score, r, c, d)
    # # if we have not seen this state or we have seen it with the same score
    if ((r, c, d) not in seen or seen[(r, c, d)] == score):
        prev[(r, c, d)].add((pr, pc, pd))
    if (r, c, d) in seen:
        continue
    seen[(r, c, d)] = score

    if grid[r][c] == "E":
        if best_score != -1 and score > best_score:
            break
        print("found", score)
        best_score = score

    for dd in D[d]:
        # print(dd)
        heappush(q, (score + 1000, r, c, dd, r, c, d))
    dr, dc = M[d]
    if grid[r + dr][c + dc] != "#":
        heappush(q, (score + 1, r + dr, c + dc, d, r, c, d))

seen = set()
part_of_path = set()
q = deque()
for ed in D.keys():
    q.appendleft((end[0], end[1], ed))

print(prev)

while q:
    r, c, d = q.pop()
    part_of_path.add((r, c))
    if (r, c, d) in seen:
        print("skipped", r, c, d)
        continue
    seen.add((r, c, d))

    for pr, pc, pd in prev[(r, c, d)]:
        q.appendleft((pr, pc, pd))
# backgrack
#
"""
for r in range(nr):
    for c in range(nc):
        if (r, c) in part_of_path and grid[r][c] not in "SE":
            print("O", end="")
            continue
        print(grid[r][c], end="")
    print()
"""
print(len(part_of_path) - 1)