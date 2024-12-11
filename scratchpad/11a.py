

with open("11.txt") as f:
    stones = [n for n in f.read().strip().split()]

print(stones)

for i in range(25):
    print(i)
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            middle = (len(stone) // 2)
            # print(stone[:middle], stone[middle:])
            new_stones.append(str(int(stone[:middle])))
            new_stones.append(str(int(stone[middle:])))
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones

    # print(" ".join(stones))

print(len(stones))
