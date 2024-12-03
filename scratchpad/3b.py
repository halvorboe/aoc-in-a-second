
with open("3.txt") as f:
    data = f.read()
    # data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def parse(s):
    print(data)
    p = 0
    s = 0
    enabled = True
    while p < len(data):
        # print(data[p:p+7])
        if data[p:p+4] == "mul(":
            p += 4
            if data[p].isdigit():
                a, p = parse_num(data, p)
                if data[p] == ",":
                    p += 1
                    if data[p].isdigit():
                        b, p = parse_num(data, p)
                        if data[p] == ")":
                            p += 1
                            print("mul", a, b, enabled)
                            if enabled:
                                s += a * b
        elif data[p:p+4] == "do()":
            print("do")
            enabled = True
            p += 4
        elif data[p:p+7] == "don't()":
            print("don't")
            enabled = False
            p += 6
        else:
            p += 1
    print(s)

def parse_num(s, p):
    k = 0
    while s[p + k].isdigit():
        k += 1
    return int(s[p:p+k]), p+k


parse(data)