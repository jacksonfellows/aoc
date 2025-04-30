import sys

def inc(password):
    i = len(password)-1
    while i >= 0:
        if password[i] == "z":
            password[i] = "a"
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return password

def valid(password):
    if any(x in password for x in "iol"): return False
    triple = False
    for i in range(len(password)):
        if i+2 < len(password) and ord(password[i]) == ord(password[i+1])-1 and ord(password[i]) == ord(password[i+2])-2: triple = True
    n_pairs = 0
    i = 0
    while i < len(password):
        if i+1 < len(password) and password[i] == password[i+1]:
            n_pairs += 1
            i += 2
        else:
            i += 1
    return triple and n_pairs > 1

password = inc(list(sys.stdin.read().strip()))
while not valid(password): password = inc(password)
print("".join(password))
