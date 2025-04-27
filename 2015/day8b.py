import sys

diff = 0
for line in sys.stdin.readlines():
    line = line.strip()
    assert line[0] == "\"" and line[-1] == "\""
    diff += 4
    i = 1
    while i < len(line) - 1:
        if line[i] == "\\" and line[i+1] == "x":
            diff += 1
            i += 4
        elif line[i] == "\\":
            diff += 2
            i += 2
        else:
            i += 1
print(diff)
