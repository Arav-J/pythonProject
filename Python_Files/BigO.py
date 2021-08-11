from turtledemo.forest import start

import end as end
from bs4 import element


def big_solution(n):
    solutions = 0
    for a in range(n+1):
        for b in range(n+1):
            c = n - (a+b)
            if c >= 0:
                solutions += 1
    return solutions

# Let f(n) and g(n) be functions from positive integers to positive reals.
# f = O(g) if there is a constant c > 0 such that f(n) is less than or equal
# to c multiplied by g(n) for large n.

list.index(element, start, end)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 42, 9, 10]
my_list.index(3)