
with open("3.txt") as f:
    data = f.read()


def parse(s):
    print(data)
    p = 0
    s = 0
    while p < len(data):
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
                            print("mul", a, b)
                            s += a * b
        else:
            p += 1
    print(s)

def parse_num(s, p):
    k = 0
    while s[p + k].isdigit():
        k += 1
    return int(s[p:p+k]), p+k


parse(data)