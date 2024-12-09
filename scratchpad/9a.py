with open("9.txt") as f:
    data = [int(n) for n in f.read().strip()]

data_section = True
disk = []
for i, n in enumerate(data):
    if data_section:
        for _ in range(n):
            disk.append(str(i // 2))
    else:
        for _ in range(n):
            disk.append(".")
    data_section = not data_section

free_pointer = 0
moving_pointer = len(disk) - 1
while free_pointer < moving_pointer:
    if disk[free_pointer] != ".":
        free_pointer += 1
    elif disk[moving_pointer] == ".":
        moving_pointer -= 1
    else:
        disk[free_pointer] = disk[moving_pointer]
        disk[moving_pointer] = "."
        free_pointer += 1
        moving_pointer -= 1


s = 0
for i, n in enumerate(disk):
    if n == ".":
        break
    # print(i, n)
    s += i * int(n)

print(s)
