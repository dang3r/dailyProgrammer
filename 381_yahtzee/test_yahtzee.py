from collections import defaultdict
import os

import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/
"""

def score(rolls: list) -> int:
    """Return the maximum yahtzee score for a given set of rolls"""
    d = defaultdict(int)
    max_score = 0 
    for val in rolls:
        d[val] += 1
        max_score = max(max_score, val * d[val])
    return max_score


dir_path = os.path.dirname(os.path.realpath(__file__))
fname = os.path.join(dir_path, "yahtzee-upper-1.txt") 
with open(fname, "r") as f:
    upper = [int(token) for token in f.read().split("\n")]

inputs = [
    ([2,3,5,5,6], 10),
    ([1,1,1,1,3], 4),
    ([1,1,1,3,3], 6),
    ([1,2,3,4,5], 5),
    ([6,6,6,6,6], 30),
    ([1654, 1654, 50995, 30864, 1654, 50995, 22747,
    1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
    30864, 4868, 30864], 123456),
    (upper, 31415926535)
]

@pytest.mark.parametrize("test_input,output", inputs)
def test_eval(test_input, output):
    assert score(test_input) == output
