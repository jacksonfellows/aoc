import itertools
import sys

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

directional_rc = {
    "^": (0,1),
    "A": (0,2),
    "<": (1,0),
    "v": (1,1),
    ">": (1,2),
}

dr = {"^":-1,"v":1,"<":0,">":0}
dc = {"^":0,"v":0,"<":-1,">":1}

def all_paths(start, end, rc_lookup, invalid_rc):
    r1,c1 = rc_lookup[start]
    r2,c2 = rc_lookup[end]
    path_elements = []
    if r2 > r1: path_elements += ["v"]*(r2-r1)
    if r1 > r2: path_elements += ["^"]*(r1-r2)
    if c2 > c1: path_elements += [">"]*(c2-c1)
    if c1 > c2: path_elements += ["<"]*(c1-c2)
    for path in set("".join(x) for x in itertools.permutations(path_elements)):
        # See if we go over the gap.
        r, c = r1, c1
        bad = False
        for step in path:
            r, c = r + dr[step], c + dc[step]
            if (r, c) == invalid_rc:
                bad = True
                break
        if not bad:
            yield path + "A"

def numeric_paths(start, end):
    yield from all_paths(start, end, numeric_rc, (3, 0))

def directional_paths(start, end):
    yield from all_paths(start, end, directional_rc, (0, 0))

def paths_for_code(code, pathf):
    paths = set([""])
    for start, end in zip("A" + code[:-1], code):
        exts = pathf(start, end)
        paths = set(path + ext for path,ext in itertools.product(paths, exts))
    return paths

def min_len(code):
    minlen = float("inf")
    for d1 in paths_for_code(code, numeric_paths):
        for d2 in paths_for_code(d1, directional_paths):
            for d3 in paths_for_code(d2, directional_paths):
                minlen = min(minlen, len(d3))
    return minlen


complexity = 0
for line in sys.stdin.readlines():
    code = line.strip()
    assert code[-1] == "A"
    L = min_len(code)
    num_code = int(code[:-1])
    print(code, num_code, L)
    complexity += L*num_code
print(complexity)
