import re
import sys
from math import floor


def read_stdin():
    m = re.search("Register A: ([0-9]+)\nRegister B: ([0-9]+)\nRegister C: ([0-9]+)\n\nProgram: (.+)$", sys.stdin.read())
    registers = [int(m[1]), int(m[2]), int(m[3])] # A, B, C
    program = list(map(int, m[4].split(",")))
    return registers, program

def run(registers, program):
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
            registers[0] = floor(registers[0]/(2**combo(operand)))
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
            output.append(combo(operand) % 8)
        elif opcode == 6:
            registers[1] = floor(registers[0]/(2**combo(operand)))
        elif opcode == 7:
            registers[2] = floor(registers[0]/(2**combo(operand)))
        else:
            assert False
        if not did_jump:
            ip += 2
    return output

if __name__ == "__main__":
    print(",".join(map(str, run(*read_stdin()))))
