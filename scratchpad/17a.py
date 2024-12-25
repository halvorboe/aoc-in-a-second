with open("17.txt") as f:
    registers, instructions = f.read().split("\n\n")

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

ip = 0
a, b, c = registers
output = []

while ip + 1 < len(instructions):
    opcode = instructions[ip]
    operand = instructions[ip + 1]
    print(opcode, operand)



    if opcode == 0:
        denominator = 2 ** combo(operand)
        a = a // denominator
    elif opcode == 1:
        b = b ^ operand
    elif opcode == 2:
        b = combo(operand) % 8
    elif opcode == 3:
        if a != 0:
            ip = operand
            continue
    elif opcode == 4:
        b = b ^ c
    elif opcode == 5:
        output.append(combo(operand) % 8)
    elif opcode == 6:
        denominator = 2 ** combo(operand)
        b = a // denominator
    elif opcode == 7:
        denominator = 2 ** combo(operand)
        c = a // denominator

    ip += 2

print(",".join(str(n) for n in output))