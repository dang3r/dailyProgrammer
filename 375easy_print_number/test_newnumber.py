import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/
todo: there must be a way to parametrize the function being called in a test
"""

def solve_str(i: int) -> int:
    return int("".join(str(int(char) + 1) for char in str(i)))

def solve_int(i: int) -> int:
    if i == 0:
        return 1
    ret = 0
    cnt = 0
    while i != 0:
        tmp = (i % 10) + 1
        i //= 10
        ret += tmp * 10 ** cnt
        # Increase exponent if tmp is 10
        if tmp == 10:
            cnt += 1
        cnt += 1
    return ret

test_cases = [
    ((998), (10109)),
    ((293), (3104)),
    ((9999), (10101010)),
    ((0), (1))
]

@pytest.mark.parametrize("_in,out", test_cases)
def test_solve(_in, out):
    assert solve_str(_in) == out

@pytest.mark.parametrize("_in,out", test_cases)
def test_bonus(_in, out):
    assert solve_int(_in) == out