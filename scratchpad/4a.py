
with open("4.txt") as f:
    data = [[ c for c in line.strip() ] for line in f]


D =  ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

"""
def look_for_word(r, c, word):
    if len(word) == 1 and word[0] == data[r][c]:
        print("found", r, c)
        return True
    elif word[0] != data[r][c]:
        return False
    print(r, c, data[r][c])
    for dr, dc in D:
        if 0 <= r + dr < len(data) and 0 <= c + dc < len(data[0]):
            if data[r + dr][c + dc] == word[1]:
                if look_for_word(r + dr, c + dc, word[1:]):
                    return True
    return False
"""

def look_for_word(r, c, word):
    s = 0
    for dr, dc in D:
        for i in range(len(word)):
            if 0 <= r + i * dr < len(data) and 0 <= c + i * dc < len(data[0]):
                if data[r + i * dr][c + i * dc] != word[i]:
                    break
            else:
                break
        else:
            # print("found", r, c)
            s += 1
    return s

print(data)
s = 0

for r in range(len(data)):
    for c in range(len(data[r])):
        #print("---")
        s += look_for_word(r, c, "XMAS")

print(s)