import re
import sys

inputs = []
num = int(raw_input())

for index in range(num):
    print bool(re.match(r"^[+-]?\d*\.\d+$", raw_input()))

