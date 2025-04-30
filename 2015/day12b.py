import sys
import json

def sum_(obj):
    if type(obj) == dict and any("red"==x for x in obj.values()): return 0
    if type(obj) == dict:
        sum__ = 0
        for k,v in obj.items():
            sum__ += sum_(k) + sum_(v)
        return sum__
    elif type(obj) == list:
        sum__ = 0
        for x in obj:
            sum__ += sum_(x)
        return sum__
    elif type(obj) == str:
        return 0
    elif type(obj) == int:
        return obj

d = json.loads(sys.stdin.read())
print(sum_(d))

