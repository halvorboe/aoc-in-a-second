
from collections import defaultdict, deque


def mix(n, sn):
    return n ^ sn

def prune(n):
    return n % 16777216

assert mix(15, 42) == 37
assert prune(100000000) == 16113920

with open("22.txt") as f:
    numbers = [int(n.strip()) for n in f]

print(numbers)

s = 0
# numbers = [123]
# SEQ = (-1,-1,0,2)
SEQ = (-2,1,-1,3)
seqs = defaultdict(lambda: 0)

for secret_number in numbers:
    current_price = secret_number % 10
    current_seq = deque()
    current_seqs = dict()
    for i in range(2000):
        secret_number = prune(mix(secret_number * 64, secret_number))
        secret_number = prune(mix(secret_number // 32, secret_number))
        secret_number = prune(mix(secret_number * 2048, secret_number))
        # print(secret_number)
        next_price = secret_number % 10
        # print(secret_number, current_price, next_price)
        change = next_price - current_price
        # print(current_seq)
        current_seq.append(change)
        if len(current_seq) > 4:
            current_seq.popleft()
        seq = tuple(current_seq)
        # print(seq, next_price)
        if seq not in current_seqs:
            current_seqs[seq] = next_price
        # print(current_seq, list((a, b) for a, b in zip(current_seq, SEQ)))
        current_price = next_price

    for key, value in current_seqs.items():
        seqs[key] += value

print(max(seqs.items(), key=lambda x: x[1]))