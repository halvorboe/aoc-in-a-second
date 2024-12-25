

with open("15.txt") as f:
    grid, moves = f.read().split("\n\n")


grid = [list(l) for l in grid.splitlines()]
moves = moves.strip().replace("\n", "")


nr = len(grid)
nc = len(grid[0]) * 2

robot = (-1, -1)
boxes = []
walls = set()

for r in range(nr):
    for c in range(nc // 2 ):
        if grid[r][c] == "@":
            grid[r][c] = "."
            robot = (r, c * 2)
        elif grid[r][c] == "O":
            grid[r][c] = "."
            boxes.append(((r, c * 2), (r, c * 2 + 1)))
        elif grid[r][c] == "#":
            walls.add((r, c * 2))
            walls.add((r, c * 2 + 1))

print(robot)

def display(ro):
    for r in range(nr):
        for c in range(nc):
            if (r, c) == ro:
                print("@", end="")
            elif (r, c) in walls:
                print("#", end="")
            elif any((r, c) == b[0] for b in boxes):
                print("[", end="")
            elif any((r, c) == b[1] for b in boxes):
                print("]", end="")
            else:
                print(".", end="")
        print()
    print()

display(robot)

def can_move(d, p):
    r, c = p
    dr, dc = d
    cr, cc = r + dr, c + dc
    if (cr, cc) in walls:
        return (False, [])
    hits = [b for b in boxes if b[0] == (cr, cc) or b[1] == (cr, cc)]
    for b in hits:
        cm, ahits = can_move_box(b, d)
        if not cm:
            return False, []
        hits.extend(ahits)
    # print(hits)
    # print("can_move", d, p)
    return (True, hits)

def can_move_box(b, d):
    p, q = b
    # print(p, q, d)

    hits = []
    if d != (0, 1):
        pcr, pcc = p
        pcr += d[0]
        pcc += d[1]
        if (pcr, pcc) in walls:
            return (False, [])
        phits = [b for b in boxes if b[0] == (pcr, pcc) or b[1] == (pcr, pcc)]
        # print("phits", phits)
        hits.extend(phits)
    if d != (0, -1):
        qcr, qcc = q
        qcr += d[0]
        qcc += d[1]
        if (qcr, qcc) in walls:
            return (False, [])
        qhits = [b for b in boxes if b[0] == (qcr, qcc) or b[1] == (qcr, qcc)]
        # print("qhits", qhits)
        hits.extend(qhits)

    for i in range(len(hits)):
        cm, h = can_move_box(hits[i], d)
        if not cm:
            return (False, [])
        hits.extend(h)

    return (True, hits)

def do_move(d, b):
    for p, q in set(b):
        pr, pc = p
        qr, qc = q
        dr, dc = d
        npr, npc = pr + dr, pc + dc
        nqr, nqc = qr + dr, qc + dc
        i = boxes.index((p, q))
        boxes[i] = ((npr, npc), (nqr, nqc))



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

    cm, b = can_move(d, robot)
    # print(cm, b)
    if cm:
        do_move(d, b)
        robot = (robot[0] + d[0], robot[1] + d[1])
    # display(robot)
    """
    if cm:
        robot = (robot[0] + d[0], robot[1] + d[1])
    if p:
        grid[p[0]][p[1]] = "O"
        grid[robot[0]][robot[1]] = "."
    """

display(robot)


s = 0
for r, c in [b[0] for b in boxes]:
    s += r * 100 + c
print(s)
