

with open("17.txt") as f:
    registers, instructions = f.read().split("\n\n")
    # lines = f.read().splitlines()

registers = [int(r.split(":")[1].strip()) for r in registers.split("\n")]
instructions = [int(i) for i in instructions.split(":")[1].strip().split(',')]

print(registers)
print(instructions)

def combo(operand):
    if 0 <= operand <= 3:
        operand_value = operand
    elif operand == 4:
        operand_value = a
    elif operand == 5:
        operand_value = b
    elif operand == 6:
        operand_value = c
    else:
        raise ValueError(f"Unknown operand {operand}")
    return operand_value

def pretty_combo(operand):
    if 0 <= operand <= 3:
        operand_value = str(operand)
    elif operand == 4:
        operand_value = "A"
    elif operand == 5:
        operand_value = "B"
    elif operand == 6:
        operand_value = "C"
    else:
        raise ValueError(f"Unknown operand {operand}")
    return operand_value

a = 0
b = 0
c = 2 ** 64 - 1

ip = len(instructions) - 4

# starting off we know we need a to be 0


while True:
    opcode = instructions[ip]
    operand = instructions[ip + 1]
    print(opcode, operand)


    if opcode == 0:
        print("adv", pretty_combo(operand))
        denominator = 2 ** combo(operand)
        a = denominator * a
    elif opcode == 1:
        print("bxl", operand)
        b = b ^ operand
    elif opcode == 2:
        print("bst", pretty_combo(operand))
        b = combo(operand) % 8
    elif opcode == 3:
        print("jmp", pretty_combo(operand))
        if a == 0:
            print("error")
    elif opcode == 4:
        print("bxc", "C")
        b = b ^ c
    elif opcode == 5:
        print("out", combo(operand) % 8)
    elif opcode == 6:
        print("bdv", pretty_combo(operand))
        denominator = 2 ** combo(operand)
        b = a * denominator
    elif opcode == 7:
        print("cdv", pretty_combo(operand))
        denominator = 2 ** combo(operand)
        c = a * denominator


    ip -= 2
    print(ip)
    if ip <= 0:
        break
