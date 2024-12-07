
with open("7.txt") as f:
    a, b= zip(*[l.split(":") for l in f])
    tests = list(zip((int(n) for n in a), ([int(n) for n in c.strip().split(" ")] for c in b)))

def matches_test(target_value, current_value, remaining_values, op="S"):
    print("match", target_value, current_value, remaining_values, op)
    if len(remaining_values) == 0:
        return current_value == target_value
    else:
        # plus
        if matches_test(target_value, current_value + remaining_values[0], remaining_values[1:], op="+"):
            return True
        # multiply
        if matches_test(target_value, current_value * remaining_values[0], remaining_values[1:], op="*"):
            return True

    return False


s = 0
for test in tests:
    if matches_test(test[0], test[1][0], test[1][1:]):
        s += test[0]

print(s)