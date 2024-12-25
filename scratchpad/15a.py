

with open("15.txt") as f:
    grid, moves = f.read().split("\n\n")


grid = [list(l) for l in grid.splitlines()]
moves = moves.strip().replace("\n", "")


nr = len(grid)
nc = len(grid[0])

robot = (-1, -1)

for r in range(nr):
    for c in range(nc):
        if grid[r][c] == "@":
            grid[r][c] = "."
            robot = (r, c)

print(robot)

def display(g, ro):
    for r in range(nr):
        for c in range(nc):
            if (r, c) == ro:
                print("@", end="")
            else:
                print(grid[r][c], end="")
        print()
    print()

display(grid, robot)

def can_move(d, p):
    r, c = p
    dr, dc = d
    # print("can_move", d, p)
    if grid[r + dr][c + dc] == "#":
        return (False, None)
    elif grid[r + dr][c + dc] == ".":
        return (True, None)
    elif grid[r + dr][c + dc] == "O":
        b, p = can_move(d, (r + dr, c + dc))
        if b and p:
            return (True, p)
        elif b:
            return (True, (r + dr * 2, c + dc * 2))
        else:
            return (False, None)
    else:
        raise ValueError("Unknown cell")



for move in moves:
    if move == "^":
        d = (-1, 0)
    elif move == "v":
        d = (1, 0)
    elif move == ">":
        d = (0, 1)
    elif move == "<":
        d = (0, -1)
    else:
        raise ValueError("Unknown move" + move)

    cm, p = can_move(d, robot)
    # print(cm, p)
    if cm:
        robot = (robot[0] + d[0], robot[1] + d[1])
    if p:
        grid[p[0]][p[1]] = "O"
        grid[robot[0]][robot[1]] = "."

display(grid, robot)

s = 0
for r in range(nr):
    for c in range(nc):
        if grid[r][c] == "O":
            s += r * 100 + c

print(s)