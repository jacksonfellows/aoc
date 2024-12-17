from math import floor

# from day17a import read_stdin


def run_match(registers, program):
    A = registers[0]
    def combo(x):
        if 0 <= x <= 3:
            return x
        if 4 <= x <= 6:
            return registers[x-4]
        assert False

    output = []
    ip = 0
    while ip < len(program):
        opcode, operand = program[ip], program[ip+1]
        did_jump = False
        if opcode == 0:
            registers[0] = registers[0] >> combo(operand)
        elif opcode == 1:
            registers[1] = registers[1] ^ operand
        elif opcode == 2:
            registers[1] = combo(operand) % 8
        elif opcode == 3:
            if registers[0] != 0:
                ip = operand
                did_jump = True
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5:
            o = combo(operand) % 8
            if program[len(output)] != o:
                return False
            output.append(o)
        elif opcode == 6:
            registers[1] = registers[0] >> combo(operand)
        elif opcode == 7:
            registers[2] = registers[0] >> combo(operand)
        else:
            assert False
        if not did_jump:
            ip += 2
    return output

registers = [0, 0, 0]
program = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]

N = 18

firsts = [0]

for _ in range(10):
    next_firsts = set()
    print("len:", len(firsts), _)
    for x in range(1,1<<N):
        for f in firsts:
            A = (x << (_*N)) + f
            registers[0] = A
            registers[1] = 0
            registers[2] = 0
            output = run_match(registers, program)
            if output:
                print(output)
                print(bin(A))
                next_firsts.add(A)
    firsts = next_firsts
