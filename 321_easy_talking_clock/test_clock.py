import pytest

numbers = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

imap = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty"
}
imap.update(enumerate(numbers))


def human_time(time: str) -> str:
    h, m = map(int, time.split(":"))

    # AM vs. PM
    half = "am" if h < 12 else "pm"
    # Get hour
    hstr = "twelve" if h % 12 == 0 else imap[h % 12]
    
    # Minutes
    if m == 0:
        return f"It's {hstr} {half}"

    tens = imap[m - m % 10]
    mins = imap[m%10]
    if m in imap:
        if 1 <= m <= 9:
             return f"It's {hstr} oh {mins} {half}"
        return f"It's {hstr} {imap[m]} {half}"

    return f"It's {hstr} {tens} {mins} {half}"




_input = [
    "00:00",
    "01:30",
    "12:05",
    "14:01",
    "20:29",
    "21:00"
]
output = [
"It's twelve am",
"It's one thirty am",
"It's twelve oh five pm",
"It's two oh one pm",
"It's eight twenty nine pm",
"It's nine pm",
]
test_cases = zip(_input, output)

@pytest.mark.parametrize("test_input,output", test_cases)
def test_eval(test_input, output):
    assert human_time(test_input) == output

