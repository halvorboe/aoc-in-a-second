



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

for secret_number in numbers:
    for _ in range(2000):
        secret_number = prune(mix(secret_number * 64, secret_number))
        secret_number = prune(mix(secret_number // 32, secret_number))
        secret_number = prune(mix(secret_number * 2048, secret_number))
    print(secret_number)
    s += secret_number

print(s)