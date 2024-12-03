
with open("1a_test.txt") as f:
    data = [line.strip().split() for line in f.read().splitlines() if line]

list_a = []
list_b = []

for a, b in data:
    a, b = int(a), int(b)
    list_a.append(a)
    list_b.append(b)

list_a.sort()
list_b.sort()

s = 0
for a, b in zip(list_a, list_b):
    print(a, b)
    dist = abs(a - b)
    s += dist

print(list_a)
print(list_b)
print(s)
