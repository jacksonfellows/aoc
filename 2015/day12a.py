import sys
import re
r = re.compile("-?[0-9]+")
sum_ = 0
for m in r.findall(sys.stdin.read()): sum_ += int(m)
print(sum_)
