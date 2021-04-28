"""Beginning of solution for https://projecteuler.net/problem=752"""
from sympy import *

def solve_n(num):
    """Calculate and return a, b where a is α(n) and b is β(n), per the prompt"""
    a, b, n = symbols("a b n")
    poly = (1 + 7**(.5))**n
    # poly = solve((a + b*math.sqrt(7))**n, a, b)
    ans = poly.subs(n, num)
    print(poly) # Remove this line once this function works
    print(ans) # Remove this line once this function works
    # return answer as a, b where a is α(n) and b is β(n)
    return 1, 1 # FIXME

# Sanity check (delete once solve_n works)
solve_n(1) # returns 1, 1
solve_n(2) # returns 8, 2
solve_n(3) # returns 22, 10

def solve_x(x):
    """For a given number x we define g(x) to be the smallest positive integer n such that:
    α(n) == 1   (mod x)
    β(n) == 0   (mod x)
    or 0 if there is no such value n.
    """
    for i in range(1, x**2): # x^2 was an educated gues at when to stop looking
        a, b = solve_n(i)
        if a % x == 1 and b % x == 0:
            return i
    return 0

# Now find and print the solution
sum = 0
for i in range(2, 1000): # Change 1000 to 1000000 for the actual solution
    sum += solve_x(i)

print(sum)
