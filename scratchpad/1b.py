from collections import Counter

with open("1a_test.txt") as f:
    data = [line.strip().split() for line in f.read().splitlines() if line]

list_a = []
list_b = []

for a, b in data:
    a, b = int(a), int(b)
    list_a.append(a)
    list_b.append(b)

counts = Counter(list_b)

s = 0
for a in list_a:
    s += counts[a] * a

print(list_a)
print(counts)

print(s)
