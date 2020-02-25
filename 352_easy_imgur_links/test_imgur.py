import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/7yyt8e/20180220_challenge_352_easy_making_imgurstyle/
- was initially confused because the 
"""

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
base = len(alphabet)

def encode(num: int) -> str:
    if num == 0:
        return "0"
    s = ""
    while num:
        right = num % base
        s += str(alphabet[right])
        num //= base
    return s

ins = [
    15674,
    7026425611433322325,
    187621,
    237860461,
    2187521,
    18752,
    0
]

outs = [
    "O44",
    "bDcRfbr63n8",
    "9OM",
    "3n26g",
    "B4b9",
    "sS4",
    "0"
]

test_cases = zip(ins ,outs)

@pytest.mark.parametrize("test_input,output", test_cases)
def test_eval(test_input, output):
    assert encode(test_input) == output