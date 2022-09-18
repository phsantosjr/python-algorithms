"""
In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, 31131211131221, ... (sequence A005150 in the OEIS).
To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, one 1" or 1211.
1211 is read off as "one 1, one 2, two 1s" or 111221.
111221 is read off as "three 1s, two 2s, one 1" or 312211.


Source: https://en.wikipedia.org/wiki/Look-and-say_sequence

"""
from typing import Union


def next_number(s: Union[str, int]):
    s = str(s)
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(f"{count}{s[i]}")
        i += 1
    return "".join(result)


def main():
    print(next_number("1"))
    assert "21", next_number("1")

    s = "1"
    n = 4
    for i in range(n - 1):
        s = next_number(s)
        print(s)


if __name__ == "__main__":
    main()
