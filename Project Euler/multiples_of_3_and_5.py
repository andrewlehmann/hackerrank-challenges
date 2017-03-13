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

def set_last_iter(n): 
    # oh god please dont look at this function
    last_iter = [0, 0, 0]
    found = [False, False, False] 
    # set to true when last iter is found for each num

    for num in range(n, n - 15, -1):
        if num <= 0:  # base case
            break

        if num % 15 == 0: 
            # finds largest multiple of 15 that is less than n
            if True not in found:
                last_iter = [num, num, num]
                break
            elif found[1] == False:
                last_iter[1] = num
                found[1] = True
            last_iter[2] = num
            found[2] = True

        elif num % 5 == 0:
            if found[1] == False: 
                # if 5 has not already been found
                last_iter[1] = num
                found[1] = True

        elif num % 3 == 0: 
            if found[0] == False:
                last_iter[0] = num
                found[0] = True
        if False not in found: 
            # if all found, break
            break
    return last_iter 

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        total = 0
        n = int(input().strip()) 

        first_iter = set_first_iter(n - 1)
        last_iter = set_last_iter(n - 1)
        num_of_iters = [math.floor((n - 1) / 3), 
                        math.floor((n - 1) / 5), 
                        math.floor((n - 1) / 15)]
        # using >> 1 to divide by 2 due to some 
        # odd behavior regarding rounding behavior
        sum_threes = (num_of_iters[0]  \
                      * (first_iter[0] \
                      + last_iter[0])) \
                      >> 1
        sum_fives = (num_of_iters[1]  \
                     * (first_iter[1] \
                     + last_iter[1])) \
                     >> 1
        sum_fifteens = (num_of_iters[2]  \
                        * (first_iter[2] \
                        + last_iter[2])) \
                        >> 1

        total = sum_threes+ sum_fives - sum_fifteens
        print(total)
