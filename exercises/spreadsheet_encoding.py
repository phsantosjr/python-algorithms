"""
Given letter for a column this program should return the ith position for this column

Example:
    Column 'A' = 1
    Column 'B' = 2
    Column 'C' = 3

    And go on


Source: https://www.youtube.com/watch?v=GDFVTZ-kKl0&list=PL5tcWHG-UPH1K7oTJgIbWy6rCMc8-8Lfm&index=7&ab_channel=LucidProgramming
"""
import string


alphabet = string.ascii_uppercase


def spreadsheet_encode_column(col: str) -> int:
    num = 0
    count = len(col) - 1
    for s in col:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num


def spreadsheet_encode_column_v2(col: str) -> int:
    dicts_ord = {ch: ord(ch) - 64 for ch in alphabet}
    num = 0
    count = len(col) - 1
    for s in col:
        ord_value = dicts_ord[s]
        num += 26**count * ord_value
        count -= 1
    return num


def main():
    column = "A"
    column_num = spreadsheet_encode_column(column)
    print(f"Column {column} is equal to {column_num}")
    assert 1, column_num

    column_num = spreadsheet_encode_column_v2(column)
    print(f"Column {column} is equal to {column_num}")
    assert 27, column_num

    column = "AA"
    column_num = spreadsheet_encode_column(column)
    print(f"Column {column} is equal to {column_num}")
    assert 27, column_num

    column_num = spreadsheet_encode_column_v2(column)
    print(f"Column {column} is equal to {column_num}")
    assert 1, column_num


if __name__ == "__main__":
    main()

