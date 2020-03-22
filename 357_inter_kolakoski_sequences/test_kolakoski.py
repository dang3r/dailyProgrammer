
from collections import Counter

import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/8df7sm/20180419_challenge_357_intermediate_kolakoski/
- I had no idea wtf the problem statement was. The key was knowing that iteration
  and the output were two different sequences.
- A run-lenngth encoding describes how many times a character is repeated prior to the character
    eg. AAABCCD -> 3A1B2C1D
- I really liked the solution at https://www.reddit.com/r/dailyprogrammer/comments/8df7sm/20180419_challenge_357_intermediate_kolakoski/dxn3yj2?utm_source=share&utm_medium=web2x
- Great explanation of `yield from` at https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-new-yield-from-syntax-in-python-3
- Key insight : since the iterator goes from odd -> even -> odd (duh), no for loop is needed
- did not do the bonus
"""

def kolakoski():
    output = [1,2,2]
    yield from output

    iteration = 2
    while True:
        # Output is 1-indexed
        size = output[iteration]
        char = 1 if (iteration+1) %2 == 1 else 2
        for _ in range(size):
            output.append(char)
            yield char
        iteration += 1
        

def gen_limit(gen, max: int):
    for i, val in enumerate(gen()):
        if i == max:
            break
        yield val


def ratio(seq):
    c = Counter(seq)
    return c[1], c[2]

test_cases = [
    (10, (5,5)),
    (100, (49, 51)),
    (1000, (502, 498))
]

@pytest.mark.parametrize("test_input,output", test_cases)
def test_eval(test_input, output):
    i = gen_limit(kolakoski, test_input)
    assert ratio(i) == output
