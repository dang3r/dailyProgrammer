import math
from typing import List, Tuple

import pytest

"""
- https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/
"""

tax_table = [
    (1e4, 0),
    (3e4, 0.1),
    (1e5, 0.25),
    (math.inf, 0.4),
]

def tax(income: int, tax_table: List[Tuple]) -> int:
    total = 0
    for i, vals in enumerate(tax_table):
        upper_bound, rate = vals
        lower_bound = tax_table[i-1][0] if i > 0 else 0
        total += int(rate * (min(upper_bound, income) - lower_bound))
        if income <= upper_bound:
            break
    return total

def overall_tax_rate(income: int, tax_table: List[Tuple]) -> float:
    return tax(income, tax_table) / income

def overall(tax_rate: float, tax_table: List[Tuple]) -> float:
    if tax_rate >= tax_table[-1][1]:
        return "NaN"

    lower = 0
    upper = 1e10
    inc = 60000
    while True:
        guess = overall_tax_rate(inc, tax_table)
        if abs(guess - tax_rate) <= 0.001:
            break
        elif guess > tax_rate:
            inc, upper = (inc + lower) / 2, inc
        else:
            inc, lower = (inc + upper) / 2, inc
    return inc

test_cases = [
    (0, 0),
    (10000, 0),
    (10009, 0),
    (10010, 1),
    (12000, 200),
    (56789, 8697),
    (1234567, 473326)]


@pytest.mark.parametrize("test_input,output", test_cases)
def test_eval(test_input, output):
    assert tax(test_input, tax_table) == output

def test_overall_tax_rate():
    assert overall(0.0, tax_table) <= 10000
    assert abs(overall(0.06, tax_table) - 25000) <= 2000
    assert abs(overall(0.09, tax_table) - 34375) <= 2000
    assert abs(overall(0.32, tax_table) - 256250) <= 2000
    assert overall(0.4, tax_table) == "NaN"
