from z3 import *

from itertools import product

"""
https://www.reddit.com/r/dailyprogrammer/comments/9z3mjk/20181121_challenge_368_intermediate_singlesymbol/

- is using z3 cheating?
- is there a nice greedy/search approach?
    - eg. start of with all 0s. Try to flip things squares and if it decreases
        the number of errors, proceed down the path
    - if nowhere to proceed, backtrack
"""


def square(n :int) -> str:
    s = Solver()
    bools = [[Bool(f"{i},{j}") for j in range(n)] for i in range(n)]
    for i, j in product(range(n), repeat=2):
        h = 1
        while i + h < n and j + h < n:
            corners = [bools[i][j], bools[i+1][j], bools[i][j+1], bools[i+1][j+1]]
            _sum = Sum([If(corner, 1, 0) for corner in corners])
            s.add(_sum != 0, _sum != 4)
            h += 1

    print("LOL")
    d = ""
    if s.check() == sat:
        m = s.model()
        for row in bools:
            for item in row:
                if is_true(m[item]):
                    d += "X"
                else:
                    d += "0"
            d += "\n"
    return d


def validate(s):
    d = [line for line in s.splitlines()]
    n = len(d)
    print(d, n)
    for i, j in product(range(n), repeat=2):
        h = 1
        while i + h < n and j + h < n:
            items = [d[i][j], d[i+1][j], d[i][j+1], d[i+1][j+1]]
            if set(items) == 1:
                return False
            h += 1
    return True

def test_2():
    assert validate(square(2))

def test_3():
    assert validate(square(3))

def test_4():
    assert validate(square(4))

def test_5():
    assert validate(square(5))

def test_6():
    assert validate(square(6))