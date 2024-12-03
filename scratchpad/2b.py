with open("2.txt") as f:
    data = [[int(n) for n in l.split()] for l in f]

print(data)

s = 0

for l in data:
    print(l)
    for i in range(len(l)):
        ls = l[:i] + l[i + 1:]
        print(i, ls)
        d = [a - b for a, b in zip (ls[1:], ls[:-1])]
        print(d)
        all_same_sign = all(n < 0 for n in d) or all(n > 0 for n in d)
        all_greater_than_0_less_than_4 = all(1 <= abs(n) <= 3 for n in d)
        print(all_same_sign, all_greater_than_0_less_than_4)
        if all_same_sign and all_greater_than_0_less_than_4:
            print("SAFE")
            s += 1
            break
        else:
            print("UNSAFE")

print(s)