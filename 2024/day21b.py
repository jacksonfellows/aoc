# Adapted from comments on AOC solutions reddit.

import sys
from functools import cache

numeric_rc = {
    "7": (0,0),
    "8": (0,1),
    "9": (0,2),
    "4": (1,0),
    "5": (1,1),
    "6": (1,2),
    "1": (2,0),
    "2": (2,1),
    "3": (2,2),
    "0": (3,1),
    "A": (3,2),
}
numeric_empty_rc = (3,0)

directional_rc = {
    "^": (0,1),
    "A": (0,2),
    "<": (1,0),
    "v": (1,1),
    ">": (1,2),
}
directional_empty_rc = (0,0)

def best_path(rc_lookup, empty_rc, start, end):
    endr, endc = rc_lookup[end]
    def rec(r, c, path):
        if (r, c) == empty_rc: return
        if (r, c) == (endr, endc):
            yield path + "A"
        # Try moving left, up, down, right (in order).
        if endc < c: yield from rec(r, c - 1, path + "<")
        if endr < r: yield from rec(r - 1, c, path + "^")
        if endr > r: yield from rec(r + 1, c, path + "v")
        if endc > c: yield from rec(r, c + 1, path + ">")
    # Return path with least changes of direction. Rely on min to return first
    # best path.
    n_change_dir = lambda path: sum(a != b for a,b in zip(path[:-1], path[1:]))
    return min(rec(*rc_lookup[start], ""), key=n_change_dir)

@cache
def solve(path, level):
    if level > 25:
        return len(path)
    if level == 0:
        rc_lookup, empty_rc = numeric_rc, numeric_empty_rc
    else:
        rc_lookup, empty_rc = directional_rc, directional_empty_rc
    return sum(solve(best_path(rc_lookup, empty_rc, start, end), level + 1) for start, end in zip("A" + path, path))

complexity = 0
for line in sys.stdin.readlines():
    code = line.strip()
    assert code[-1] == "A"
    L = solve(code, 0)
    num_code = int(code[:-1])
    complexity += L*num_code
print(complexity)
