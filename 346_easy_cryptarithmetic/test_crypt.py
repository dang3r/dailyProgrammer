from itertools import permutations

import pytest 

"""
https://www.reddit.com/r/dailyprogrammer/comments/7p5p2o/20180108_challenge_346_easy_cryptarithmetic_solver/
- someone did it by compiling to bytecode with a custom vm. WTF? todo: learn how it works
- solves all test cases in 47.69s
"""

def transform(s: str, mapping: dict) -> int:
    k = 0
    for i, char in enumerate(s[::-1]):
        k += mapping[char] * (10 ** i)
    return k

def solve(ops: list) -> dict:
    """The last arg is the sum, all other args are operands"""
    var = set()
    for op in ops:
        var |= set(op)
    sorted_var = sorted(var)

    for combo in permutations(range(10), len(var)):
        d = dict(zip(sorted_var, combo))
        tops = [transform(op, d) for op in ops]

        # Skip assignments with leading 0s
        if any(d[op[0]] == 0 for op in ops):
            continue

        #print(tops)
        if sum(tops[:-1]) == tops[-1]:
            print(tops)
            print(d)
            return d
    
test_cases = [
    (("SEND", "MORE", "MONEY"), dict(O=0,M=1,Y=2,E=5,N=6,D=7,R=8,S=9)),
    ("THIS IS HIS CLAIM".split(), {"A":7, "C":1, "H":8, "I":5, "L":0, "M":6, "S":2, "T":9}),
    ("WHAT WAS THY CAUSE".split(), {"A":0, "C":1, "E":4, "H":2, "S":3, "T":6, "U":7, "W":9, "Y":5}),
    ("HIS HORSE IS SLAIN".split(), {"A":1, "E":8, "H":3, "I":5, "L":0, "N":6, "O":9, "R":7, "S":4}),
    #("HERE SHE COMES".split(), ),
    ("FOR LACK OF TREAD".split(), {"A":6, "C":7, "D":3, "E":2, "F":5, "K":8, "L":9, "O":4, "R":0, "T":1}),
    ("I WILL PAY THE THEFT".split(),  {"A":2, "E":4, "F":7, "H":0, "I":8, "L":3, "P":5, "T":1, "W":9, "Y":6})
]

@pytest.mark.parametrize("case", test_cases)
def test_eval(case):
    assert solve(case[0]) == case[1]

