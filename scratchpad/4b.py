
with open("4.txt") as f:
    data = [[ c for c in line.strip() ] for line in f]


D =  ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def look_for_x(r, c):
    if data[r][c] != "A":
        return False
    down_right = data[r + 1][c + 1] + data[r - 1][c - 1]
    down_left = data[r - 1][c + 1] + data[r + 1][c - 1]
    print(data[r][c], r, c, down_left, down_right)
    if set(down_right) == set("MS") and set(down_left) == set("MS"):
        print("found", r, c)
        return True
    return False


s = 0
for r in range(1, len(data) - 1):
    for c in range(1, len(data[r]) - 1):
        #print("---")
        if look_for_x(r, c):
            s += 1

print(s)