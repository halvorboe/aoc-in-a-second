from typing import List
from functools import lru_cache

MAX = 2 ** 64

with open("21.txt") as f:
    codes = [line.strip() for line in f]

# There is

NUMS = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}
NUMS_V = set(NUMS.values())

DIRS = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}
DIRS_V = set(DIRS.values())

# Generates all valid sequences to generate a given number
def code_to_seqs(code) -> List[str]:
    possible = [""]
    current_button = "A"
    # print(code)
    for button in code:
        # print(button, possible)
        new_possible = []
        # print(current_button, NUMS[current_button], NUMS[button], button)
        (sr, sc), (er, ec) = NUMS[current_button], NUMS[button]
        for option in from_to_click_seqs(sr, sc, er, ec, NUMS_V):
            for p in possible:
                new_possible.append(p + option)
        current_button = button
        possible = new_possible
    return possible





"""
If we're at depth 0 we return the

Pressing the button at the level below always ends with pressing a so we can split it up and
return the minimum to press a

"""
@lru_cache(maxsize=None)
def seq_to_seqs(seq, depth):
    # print(seq, depth)
    current_button = "A"
    sum_shortest = 0
    for button in seq:
        # print(button, possible)
        shortest = MAX
        (sr, sc), (er, ec) = DIRS[current_button], DIRS[button]
        for option in from_to_click_seqs(sr, sc, er, ec, DIRS_V):
            if depth > 0:
                sub_shortest = seq_to_seqs(option, depth - 1)
            else:
                sub_shortest = len(option)


            shortest = min(shortest, sub_shortest)
        sum_shortest += shortest
        current_button = button

    return sum_shortest



# Generates all valid sequences between two numbers
def from_to_click_seqs(fr, fc, tr, tc, valid) -> List[str]:
    if fr == tr and fc == tc:
        return ["A"]
    possible = []
    # UP
    if fr > tr and (fr - 1, fc) in valid:
        for option in from_to_click_seqs(fr - 1, fc, tr, tc, valid):
            possible.append("^" + option)
    # DOWN
    if fr < tr and (fr + 1, fc) in valid:
        for option in from_to_click_seqs(fr + 1, fc, tr, tc, valid):
            possible.append("v" + option)
    # LEFT
    if fc > tc and (fr, fc - 1) in valid:
        for option in from_to_click_seqs(fr, fc - 1, tr, tc, valid):
            possible.append("<" + option)
    # RIGHT
    if fc < tc and (fr, fc + 1) in valid:
        for option in from_to_click_seqs(fr, fc + 1, tr, tc, valid):
            possible.append(">" + option)

    # print(fr, fc, tr, tc, possible)
    return possible

s = 0

for code in codes:
    possible = code_to_seqs(code)
    print(possible)
    final_possible = []
    for seq in possible:
        final_possible.append(seq_to_seqs(seq, depth=24))
    # print(final_possible)
    # Make sure that we don't have duplicates
    best = min(final_possible)
    s += int(code[:3]) * best
    print(code, best )

print(s)

