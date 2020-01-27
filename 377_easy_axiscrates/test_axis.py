
import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
todo: fit3
todo: fitn
todo: how to have parameterize the test function being used
"""

def fit(X: int, Y: int, x: int, y: int) -> int:
    return (X // x) * (Y // y)

def fit2(X: int, Y: int, x: int, y: int) -> int:
    return max(fit(X, Y, y, x), fit(X, Y, x, y))

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

@pytest.mark.parametrize("test_input,output", fit_test_cases)
def test_eval(test_input, output):
    assert fit(*test_input) == output

@pytest.mark.parametrize("test_input,output", fit2_test_cases)
def test_eval2(test_input, output):
    assert fit2(*test_input) == output