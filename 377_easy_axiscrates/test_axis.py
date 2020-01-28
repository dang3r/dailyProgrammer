from itertools import permutations
from typing import List

import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
- fit3 and fitn were a good challenge. I kept struggling until I realized you just had to map a a box dimension to a crate
  dimension. After that insight, you can generate permutations of indices and perform the regular calculation
todo: how to have parameterize the test function being used
"""

def fit(X: int, Y: int, x: int, y: int) -> int:
    return (X // x) * (Y // y)

def fit2(X: int, Y: int, x: int, y: int) -> int:
    return max(fit(X, Y, y, x), fit(X, Y, x, y))

def fitn(crate: List[int], box: List[int]) -> int:
    ret = 0
    for perm in permutations(range(len(box))):
        t = 1
        for i, p in enumerate(perm):
            t *= (crate[i]  // box[p])
        ret = max(ret ,t)
    return ret

def fit3(*args: List[int]) -> int:
    assert len(args) == 6
    return fitn(args[:3], args[3:])


fit_test_cases = [
    ((25, 18, 6, 5) , 12),
    ((10, 10, 1, 1) , 100),
    ((12, 34, 5, 6) , 10),
    ((12345, 678910, 1112, 1314) , 5676),
    ((5, 100, 6, 1) , 0)
]

fit2_test_cases = [
    ((25, 18, 6, 5) , 15),
    ((12, 34, 5, 6) , 12),
    ((12345, 678910, 1112, 1314) , 5676),
    ((5, 5, 3, 2) , 2),
    ((5, 100, 6, 1) , 80),
    ((5, 5, 6, 1) , 0),
]

fit3_test_cases = [
    ((10, 10, 10, 1, 1, 1) , 1000),
    ((12, 34, 56, 7, 8, 9) , 32),
    ((123, 456, 789, 10, 11, 12) , 32604),
    ((1234567, 89101112, 13141516, 171819, 202122, 232425) , 174648)
]

fitn_test_cases = [
    (([3, 4], [1, 2]) , 6),
    (([123, 456, 789], [10, 11, 12]) , 32604),
    (([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21]) , 1883443968)
]


@pytest.mark.parametrize("test_input,output", fit_test_cases)
def test_eval(test_input, output):
    assert fit(*test_input) == output

@pytest.mark.parametrize("test_input,output", fit2_test_cases)
def test_eval2(test_input, output):
    assert fit2(*test_input) == output

@pytest.mark.parametrize("test_input,output", fit3_test_cases)
def test_eval3(test_input, output):
    assert fit3(*test_input) == output

@pytest.mark.parametrize("test_input,output", fitn_test_cases)
def test_evaln(test_input, output):
    assert fitn(*test_input) == output