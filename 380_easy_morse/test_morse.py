from collections import Counter, defaultdict

import pytest

"""
https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/
Cool things learned from the python3 solutions:
- the string module has lists for ascii characters (upper and lower). Using this instead of my ord/chr solution for
  generating the morsed lookup dictionary would be cleaner
- for bonus_3, instead of counting each character type and comparing to determine if a word is balanced, use an integer instead.
  If '-', subtract 1 and if '.' add 1. Both solutions require a single linear pass of the string, but this only requires 1 int
  Its similar to the balanced parentheses question. Instead of using a stack, an integer is enough.
- for bonus_5, using itertools.product(".-", repeat=13) would prevent the scheme I used for generating different encoded words.
  The example solution also concatenated all morse codes with length >= 13. TO determine if your morse string is present, simply check
  the big string. I _really_ like this solution.]
"""

codes = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split(" ")
morsed = {chr(ord("a") + i): code for i, code in enumerate(codes)}

with open("enable1.txt", "r") as f:
    enablelst = f.read().splitlines()

test_cases = [
    ("sos", "...---..."),
    ("daily", "-...-...-..-.--"),
    ("programmer", ".--..-.-----..-..-----..-."),
    ("bits", "-.....-..."),
    ("three", "-.....-...")
]

def encode(word: str) -> str:
    return "".join([morsed[char] for char in word])

def palindrome(word: str) -> True:
    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

def bonus_1() -> str:
    d = Counter([encode(word) for word in enablelst])
    for k, cnt in d.items():
        if cnt == 13:
            print("bonus 1: ", k)
            return k

def bonus_2() -> str:
    enc = [encode(word) for word in enablelst]
    target = "-" * 15
    for morse in enc:
        if target in morse:
            print(morse)
            return morse

def bonus_3() -> str:
    words = [word for word in enablelst if len(word) == 21 and word != "counterdemonstrations"]
    for word in words:
        enc = encode(word)
        if enc.count(".") == enc.count("-"):
            print(word)
            return word

def bonus_4() -> str:
    words = [word for word in enablelst if len(word) == 13 and palindrome(encode(word))]
    assert len(words) == 1
    return words[0]

def bonus_5() -> list:
    _enc = lambda x: int(con.replace("-", "0").replace(".", "1"), base=2)
    _dec = lambda x: str(x).replace("0", "-").replace("1", ".")
    nums = set(list(range(2**13)))
    for word in enablelst:
        enc = encode(word)
        if len(enc) < 13:
            continue
        for i in range(0, len(enc) - 13):
            con = enc[i:i+13]
            _int = _enc(con)
            if _int in nums:
                nums.remove(_int)
    return [_dec(num) for num in nums]

print(bonus_5())
@pytest.mark.parametrize("test_input,output", test_cases)
def test_eval(test_input, output):
    assert encode(test_input) == output

def test_bonus_1():
    assert bonus_1() is not None

def test_bonus_2():
    assert bonus_2() is not None

def test_bonus_3():
    assert bonus_3() is not None

def test_bonus_4():
    assert bonus_4() is not None

def test_bonus_5():
    assert len(bonus_5()) == 5