import os
from collections import Counter, defaultdict

import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/
"""

fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "enable1.txt")

def variants(s1: str) -> list:
    return (s1[i:] + s1[:i] for i in range(len(s1)))

def same_necklace(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    elif s1 == s2:
        return True

    for variant in variants(s1):
        if variant == s2:
            return True
    return False

def repeats(s1: str) -> int:
    if len(s1) == 0:
        return 1
    total = 0
    for variant in variants(s1):
        if s1 == variant:
            total += 1
    return total

def bonus():
    d = defaultdict(list)
    for line in open(fname):
        line = line.strip()
        if len(line) < 4:
            continue
        c = Counter(line)
        # Group words by sorted (key, frequency) tuples
        # c.items() is not ordered, so sorting makes the key deterministic
        d[tuple(sorted(c.items(), key=lambda x: x[0]))].append(line)

    for v in d.values():
        if len(v) < 4:
            continue
        for i, variant in enumerate(v):
            s = set(variants(variant))
            similar = [a for a in v[i+1:] if a in s]
            if len(similar) == 3:
                similar.append(variant)
                return similar

test_cases = [
    (("nicole", "icolen"), True),
    (("nicole", "lenico"), True),
    (("nicole", "coneli"), False),
    (("aabaaaaabaab", "aabaabaabaaa"), True),
    (("abc", "cba"), False),
    (("xxyyy", "xxxyy"), False),
    (("xyxxz", "xxyxz"), False),
    (("x", "x"), True),
    (("x", "xx"), False),
    (("x", ""), False),
    (("", ""), True),
]

test_cases_repeats = [
    ("abc", 1),
    ("abcabcabc", 3),
    ("abcabcabcx", 1),
    ("aaaaaa", 6),
    ("a", 1),
    ("", 1),
]

@pytest.mark.parametrize("test_input,output", test_cases)
def test_eval(test_input, output):
    assert same_necklace(*test_input) == output

@pytest.mark.parametrize("test_input,output", test_cases_repeats)
def test_repeat(test_input, output):
    assert repeats(test_input) == output

def test_bonus():
    ns = bonus()
    assert len(ns) == 4
    s = set(variants(ns[0]))
    for n in ns:
        assert n in s
