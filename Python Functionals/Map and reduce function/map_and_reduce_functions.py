# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(raw_input())
fib = []

if n > 0:
    fib.append(0)
if n > 1:
    fib.append(1)
    if n > 2:
        for i in range(2, n):
            fib.append(fib[len(fib)-1] + fib[len(fib)-2])

cubes = lambda a: a ** 3
print list(map(cubes, fib))