#!/bin/python3
import math

# This program uses the summation formula to find 
# the sum of all multiples of 3 or 5 below a number n. 
# This method was chosen due to complexity reducution 
# and massive time saving on very large numbers

def set_first_iter(n):
    if(n >= 15):
        return [3, 5, 15]
    elif (n >= 5):
        return [3, 5, 0]
    elif (n >= 3):
        return [3, 0, 0]
    else:
        return [0, 0, 0]

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        total = 0
        n = int(input().strip()) 

        first_iter = set_first_iter(n - 1)
        last_iter = [(n - 1) - ((n - 1) % 3),
                     (n - 1) - ((n - 1) % 5),
                     (n - 1) - ((n - 1) % 15)]
        num_of_iters = [math.floor((n - 1) / 3), 
                        math.floor((n - 1) / 5), 
                        math.floor((n - 1) / 15)]
        # using >> 1 to divide by 2 due to some 
        # odd behavior regarding rounding behavior
        sum_threes = (num_of_iters[0] * (first_iter[0] + last_iter[0])) >> 1
        sum_fives = (num_of_iters[1] * (first_iter[1] + last_iter[1])) >> 1
        sum_fifteens = (num_of_iters[2]* (first_iter[2] + last_iter[2])) >> 1
        total = sum_threes + sum_fives - sum_fifteens
        print(total)
