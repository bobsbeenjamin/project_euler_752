"""Beginning of solution for https://projecteuler.net/problem=752"""
from sympy import *

solve_n_cache = [None] # This will purposely break if the first element is accessed

def solve_n(num):
    """Calculate and return a, b where a is α(n) and b is β(n), per the prompt"""
    if num < len(solve_n_cache):
        return solve_n_cache[num]
    poly = (1 + sqrt(7))**num
    ans = expand(poly)
    # print(ans) # Remove this line once this function works
    # print(ans.args) # Remove this line once this function works
    a = ans.args[0]
    b = 1 if str(ans.args[1]) == "sqrt(7)" else ans.args[1].args[0]
    # print(ans.args[0], b) # Remove this line once this function works
    # return answer as a, b where a is α(n) and b is β(n)
    solve_n_cache.append((a, b)) # This pushes a 2-tuple as the last element
    return a, b

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
    for i in range(1, x**2): # x^2 is an educated guess at when to stop looking
        a, b = solve_n(i)
        if a % x == 1 and b % x == 0:
            return i
    return 0

# Now find and print the solution
sum = 0
for i in range(2, 100): # Change to 1000000 for the actual solution
    sum += solve_x(i)

print(sum)
