import math

# Here we go with the number theory
# if the stone is 0 we make it 1
# don't think it matters
# if the stone is even we split it in half
# multiplying the number by 2024


"""
print(9999, number_of_digits(1234))
print(1000, number_of_digits(1000))
print(100, number_of_digits(100))
print(10, number_of_digits(10))
print(1, number_of_digits(1))

print(1234, bottom_half(1234, 2))
print(1234, top_half(1234, 2))

print(1234, bottom_half(1000, 2))
print(1234, top_half(1000, 2))

print(10 * 2024)
"""


with open("11.txt") as f:
    stones = [int(n) for n in f.read().strip().split()]

print(stones)

"""
known = {}

for stone in stones:
    print(stone)
    for i in range(10):
        if stone == 0:
            stone = 1
        elif stone % 2 == 0:
            digits = number_of_digits(stone)
            stone = top_half(stone, digits // 2)
            # print("bottom", bottom_half(stone, digits // 2))
        else:
            stone *= 2024
        print(stone, end=" ")
"""

from functools import lru_cache

def number_of_digits(n):
    return math.floor(math.log10(n)) + 1

def bottom_half(n, digits):
    return n % (10 ** digits)

def top_half(n, digits):
    return n // (10 ** digits)

@lru_cache(maxsize=None)
def compute(stone, depth):
    if depth == 0:
        # print(stone, end=" ")
        return 1
    if stone == 0:
        return compute(1, depth - 1)
    digits = number_of_digits(stone)
    if digits % 2 == 0:
        digits = digits // 2
        return compute(top_half(stone, digits), depth - 1) + compute(bottom_half(stone, digits), depth - 1)
    else:
        return compute(stone * 2024, depth - 1)

blinks = 75

s = 0

for stone in stones:
    s += compute(stone, blinks)

print(s)
