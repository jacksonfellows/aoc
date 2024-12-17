import sys
from math import floor

from day17a import read_stdin


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

_, program = read_stdin()

N = 18
prefixes = [0]
sols = set()

for _ in range(10):
    next_prefixes = set()
    for x in range(1,1<<N):
        for pre in prefixes:
            A = (x << (_*N)) + pre
            registers = [A, 0, 0]
            try:
                output = run_match(registers, program)
            except:
                print(min(sols))
                sys.exit()
            if output:
                next_prefixes.add(A)
                if len(output) == len(program):
                    sols.add(A)
    prefixes = next_prefixes
