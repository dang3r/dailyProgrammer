import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/
- learned that if you slice a list with an starting index that is out of bounds, it returns an empty list
    >>> l = [1,2,3]
    >>> l[2:]
    [3]
    >>> l[3:]
    []
    >>> l[5:]
    []
    >>> exit()
"""

def funnel(s1: str, s2: str) -> bool:
    for i in range(len(s1)):
        c = s1[:i] + s1[i+1:]
        if c == s2:
            return True
    return False

funnel_test_cases = [
    (("leave", "eave"), True),
    (("reset", "rest"), True),
    (("dragoon", "dragon"), True),
    (("eave", "leave") ,False),
    (("sleet", "lets") ,False),
    (("skiff", "ski") ,False),
]

@pytest.mark.parametrize("test_input,output", funnel_test_cases)
def test_eval(test_input, output):
    assert funnel(*test_input) == output