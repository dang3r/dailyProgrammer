import pytest


"""
https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/
"""

def digits(i: int):
    if i == 0:
        return i

    while i != 0:
        d = i % 10
        yield d
        i //= 10


def loops(d: int):
    l = 0
    while d >= 10:
        d = sum(digits(d))
        l += 1
    return l



test_cases = [
    (13, 1),
    (1234, 2),
    (9876, 2),
    (199, 3)
]


@pytest.mark.parametrize("test_input,output", test_cases)
def test_eval(test_input, output):
    assert loops(test_input) == output