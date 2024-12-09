with open("9.txt") as f:
    data = [int(n) for n in f.read().strip()]

data_section = True
disk = []
offset = 0
for i, n in enumerate(data):
    if data_section:
        disk.append((i // 2, offset, offset + n))
    offset += n
    data_section = not data_section



disk = list(disk)
final_disk = list(disk)

"""
for a, b in zip(final_disk, final_disk[1:]):
    n, s, e = a
    nn, ns, ne = b
    print(str(n) * (e - s), end="")
    print("." * (ns - e), end="")
print(str(disk[-1][0]) * (disk[-1][2] - disk[-1][1]))
print()
"""

for it in reversed(disk[1:]):
    n, f, t = it
    size = t - f
    # print(n, f, t, "size", size)
    # find a space
    p = 0
    while True:
        # print(final_disk[p], final_disk[p+1])
        an, af, at = final_disk[p]
        bn, bf, bt = final_disk[p+1]
        if bf - at >= size:
            # print("space", bf - at, at, bf)
            # print(final_disk)
            final_disk.remove(it)
            final_disk.insert(p+1, (n, at, at + size))
            # print(final_disk)
            break
        # if we have reached ourselves
        if bn == n:
            break
        p += 1

    """
    for a, b in zip(final_disk, final_disk[1:]):
        n, s, e = a
        nn, ns, ne = b
        print(str(n) * (e - s), end="")
        print("." * (ns - e), end="")
    print(str(final_disk[-1][0]) * (final_disk[-1][2] - final_disk[-1][1]))
    print()
    """

print(final_disk)
s = 0
for n, f, t in final_disk:
    for i in range(f, t):
        s += i * n

print(s)
