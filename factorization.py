#!/usr/bin/python3

import math
import random
# This is a trial to print all factors of a large number with
# pollard's rho algorithm
def algorithm(n):
    f = lambda x: ((x * x) + 1) % n
    x = 2
    value = 2
    checker = 0
    while checker < 2:
        t = f(x)
        h = f(f(x))
        d = math.gcd(abs(t - h), n)
        value = d
        if value != 1:
            return value
        checker += 1
        

    return 1

number = int(input("Enter a number: "))

success = algorithm(number)
print("the smallest factors of {} are  : {} and {}".format(number, success, number // success))


    



