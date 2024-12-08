from math import gcd
from collections import defaultdict

with open('8.txt') as f:
    grid = [l.strip() for l in f.read().splitlines()]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

antennas = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        ch = grid[r][c]
        if ch != '.':
            antennas[ch].append((r, c))

antinode_positions = set()

for freq, coords in antennas.items():
    if len(coords) < 2:
        continue
    n = len(coords)
    for i in range(n):
        for j in range(i+1, n):
            r1,c1 = coords[i]
            r2,c2 = coords[j]
            dr, dc = r2 - r1, c2 - c1
            g = gcd(dr, dc)
            dr //= g
            dc //= g

            rr, cc = r1, c1
            while 0 <= rr < rows and 0 <= cc < cols:
                antinode_positions.add((rr, cc))
                rr += dr
                cc += dc
            rr, cc = r1 - dr, c1 - dc
            while 0 <= rr < rows and 0 <= cc < cols:
                antinode_positions.add((rr, cc))
                rr -= dr
                cc -= dc

print(len(antinode_positions))
