
raw_locks = []
raw_keys = []

with open("25.txt") as f:
    for key_or_lock in (it.split("\n") for it in f.read().split("\n\n")):
        if all(c == "#" for c in key_or_lock[0]):
            raw_locks.append(key_or_lock[1:])
        elif all(c == "#" for c in key_or_lock[-1]):
            raw_keys.append(list(reversed(key_or_lock[:-1])))
        else:
            raise ValueError("Unknown key or lock", key_or_lock)

locks = []
keys = []

for raw_lock in raw_locks:
    values = [[i + 1 if c == "#" else 0 for c in l] for i, l in enumerate(raw_lock)]
    locks.append([max(v[i] for v in values) for i in range(5)])

for raw_key in raw_keys:
    values = [[i + 1 if c == "#" else 0 for c in l] for i, l in enumerate(raw_key)]
    keys.append([max(v[i] for v in values) for i in range(5)])

# print(locks)
# print(keys)
s = 0
for lock in locks:
    for key in keys:
        # print(lock, key)
        if not any(l + k > 5 for l, k in zip(lock, key)):
            s += 1
# print(raw_keys)
print(s)