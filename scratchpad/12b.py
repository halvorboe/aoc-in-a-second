
with open("12_test.txt") as f:
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
            region = set()
            compute_size(r, c, grid[r][c], seen, region)
            print(r, c, grid[r][c])
            # print(region)
            size = poligon_sides(region)
            print(size, len(region))
            score += size * len(region)
            # return
    print(score)


def poligon_sides(region):
    sides = 0

    min_r = min(r for r, c in region)
    max_r = max(r for r, c in region)
    min_c = min(c for r, c in region)
    max_c = max(c for r, c in region)

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        sides += calculate_sides_in_direction(region, min_r, max_r, min_c, max_c, dr, dc)

    return sides

def calculate_sides_in_direction(region, min_r, max_r, min_c, max_c, dr, dc):
    sides = 0
    for r in range(min_r, max_r + 1):
        flip = False
        for c in range(min_c, max_c + 1):
            state = (r, c) in region and (r + dr, c + dc) not in region

            if not flip and state:
                sides += 1

            flip = state

    return sides

def poligon_sides_2(region):
    print(region)
    counted = set()
    sides = 0
    for r, c in region:
        if (r, c) in counted:
            continue
        counted.add((r, c))
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (r + dr, c + dc) not in region:
                sides += 1
            for sign in (-1, 1):
                pdr, pdc = sign * dc, -sign * dr
                # go along the side
                cr, cc = r, c
                ccr, ccc = cr + dr, cc + dc
                while True:
                    counted.add((cr, cc))
                    if (cr + pdr, cc + pdc) in region and (ccr + pdr, ccc + pdc) not in region:
                        cr += pdr
                        cc += pdc
                        ccr += pdr
                        ccc += pdc
                    else:
                        break

    assert len(counted) == len(region)

    return sides



def poligon_size_2(region):

    seen = set()
    print(region)
    shapes = []
    for r, c in sorted(region):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        # find square
        changed = True
        er, ec = r, c
        while changed:
            changed = False
            if er < n_r:
                needed = [(er + 1, ecc) for ecc in range(c, ec + 1)]
                if all(n in region for n in needed):
                    # print("needed", needed)
                    er += 1
                    changed = True
                    for n in needed:
                        seen.add(n)
            if ec < n_c:
                needed = [(err, ec + 1) for err in range(r, er + 1)]
                if all(n in region for n in needed):
                    # print("needed", needed)
                    ec += 1
                    changed = True
                    for n in needed:
                        seen.add(n)
        shapes.append((r, c, er, ec))

    s = 0
    for sr, sc, er, ec in shapes:
        print("shape", sr, sc, er, ec)
        # up
        up = [(sr - 1, c) for c in range(sc, ec + 1)]
        if not all(n in region for n in up):
            # print("up")
            s += 1
        # print("> up", up)
        # down
        down = [(er + 1, c) for c in range(sc, ec + 1)]
        if not all(n in region for n in down):
            # print("down")
            s += 1
        # print("> down", down)
        # left
        left = [(r, sc - 1) for r in range(sr, er + 1)]
        if not all(n in region for n in left):
            # print("left")
            if (sc, sr - 1) not in region or (sc, er + 1) not in region:
                s += 1
        # print("> left", left)
        # right
        right = [(r, ec + 1) for r in range(sr, er + 1)]
        if not all(n in region for n in right):
            # print("right")
            if (ec, sr - 1) not in region or (ec, er + 1) not in region:
                s += 1
        # print("> right", right)
    return s



def compute_size(r, c, t, seen, region):
    seen.add((r, c))
    region.add((r, c))
    s = 0
    a = 1
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n_r or nc < 0 or nc >= n_c or grid[nr][nc] != t:
            # print("perimiter", nr, nc)
            s += 1
        elif (nr, nc) not in seen:
            # print("found", nr, nc)
            c_s, c_a = compute_size(nr, nc, t, seen, region)
            s += c_s
            a += c_a
        else:
            # print("skipped", nr, nc)
            pass
    # print("-> ", r, c, t, s)
    return (s, a)

# print(grid)
flood()