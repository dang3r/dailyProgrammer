from z3 import *

from itertools import product

"""
https://www.reddit.com/r/dailyprogrammer/comments/9z3mjk/20181121_challenge_368_intermediate_singlesymbol/

- is using z3 cheating?
- is there a nice greedy/search approach?
    - eg. start of with all 0s. Try to flip things squares and if it decreases
        the number of errors, proceed down the path
    - if nowhere to proceed, backtrack
- I used https://www.youtube.com/watch?v=Zq4upTEaQyM to help implement the backtracking approach. My key takeaways are
    - how you iterate through a grid solution is important. The trick to go to the next row
        if you go past the last column is nice.
    - proceed if the decision you made is valid. If not, try another decision.
        - decisions can be naive, the validation logic is what is complex
"""


def square(n :int) -> str:
    s = Solver()
    bools = [[Bool(f"{i},{j}") for j in range(n)] for i in range(n)]
    for i, j in product(range(n), repeat=2):
        h = 1
        while i + h < n and j + h < n:
            corners = [bools[i][j], bools[i+h][j], bools[i][j+h], bools[i+h][j+h]]
            _sum = Sum([If(corner, 1, 0) for corner in corners])
            s.add(_sum != 0, _sum != 4)
            h += 1

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

def square_bt(n: int):
    if n == 1:
        return "X"

    d = [["" for j in range(n)] for i in range(n)]

    def valid():
        for i, j in product(range(n), repeat=2):
            h = 1
            while i + h < n and j + h < n:
                items = [d[i][j], d[i+h][j], d[i][j+h], d[i+h][j+h]]
                if len(set(items)) == 1 and len(items[0]) == 1:
                    return False
                h += 1
        return True

    def solve(i: int, j: int):
        if j == n:
            i += 1
            j = 0
            if i == n:
                return True

        for num in "XO":
            d[i][j] = num
            if valid() and solve(i, j+1):
                return True
            d[i][j] = ""

        return False

    
    assert solve(0, 0) == True
    return "\n".join(["".join(line) for line in d])


def validate(s):
    d = [line for line in s.splitlines()]
    n = len(d)
    for i, j in product(range(n), repeat=2):
        h = 1
        while i + h < n and j + h < n:
            items = [d[i][j], d[i+h][j], d[i][j+h], d[i+h][j+h]]
            if len(set(items)) == 1:
                return False
            h += 1
    return True



def test_validate():
    assert not validate(
"""0110
1111
1111
0110""")
    assert validate(
"""OOOXX
XXOOO
OOXOX
OXOOX
XOXXO""")

def test_1():
    assert validate(square_bt(2))
    assert validate(square_bt(3))
    assert validate(square_bt(4))
    assert validate(square_bt(5))
    assert validate(square_bt(6))

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