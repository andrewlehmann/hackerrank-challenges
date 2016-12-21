# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


input = []

for item in sys.stdin:
    input.append(item)
A = set(map(int, input[2].split()))
B = set(map(int, input[3].split()))
input = map(int, input[1].split())

total = 0

for item in input:
    if item in A:
        total = total + 1
    if item in B:
        total = total - 1
        
print total
