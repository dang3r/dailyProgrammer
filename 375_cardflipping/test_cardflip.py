import pytest


"""
https://www.reddit.com/r/dailyprogrammer/comments/aq6gfy/20190213_challenge_375_intermediate_a_card/
- simple backtracking solution
"""
null = set(".0")

def solve(cards: list) -> list:
    if all([card == "." for card in cards]):
        return []
    if all([card in null for card in cards]):
        return None

    def flip(i: int):
        if i < 0 or i == len(cards) or cards[i] == ".":
            return
        cards[i] = "0" if cards[i] == "1" else "1"
            

    for i in range(len(cards)):
        if cards[i] == "1":
            cards[i] = "."
            flip(i-1)
            flip(i+1)
            ret = solve(cards)
            if ret is None:
                cards[i] = "1"
                flip(i-1)
                flip(i+1)
            else:
                return [str(i)] + ret


test_cases = [
    ("0100110", "1 0 2 3 5 4 6"),
    ("01001100111", None),
    ("100001100101000", "0 1 2 3 4 6 5 7 8 11 10 9 12 13 14"),
]

@pytest.mark.parametrize("test_input,output", test_cases)
def test_eval(test_input, output):
    ret = solve(list(test_input))
    if ret is not None:
        ret = " ".join(ret)
    assert ret == output
    #print(solve(list("0100110")))



