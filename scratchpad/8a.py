from collections import defaultdict

with open('8_test.txt') as f:
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
    n = len(coords)
    for i in range(n):
        for j in range(i+1, n):
            r1,c1 = coords[i]
            r2,c2 = coords[j]
            dx = r2 - r1
            dy = c2 - c1

            # P=A+t(B−A)
            candidates = [
                (2*r1 - r2, 2*c1 - c2),
                (r1 + 2*dx, c1 + 2*dy)
            ]

            if dx % 3 == 0 and dy % 3 == 0:
                candidates.append((r1 + dx//3, c1 + dy//3))       # t = 1/3
                candidates.append((r1 + 2*(dx//3), c1 + 2*(dy//3))) # t = 2/3

            for rr, cc in candidates:
                if 0 <= rr < rows and 0 <= cc < cols:
                    antinode_positions.add((rr, cc))

print(len(antinode_positions))
