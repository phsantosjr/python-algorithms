"""
Write a function that returns the middle letter. If there is no middle letter, your function
should return empty string
"""


def mid(text):
    text_length = len(text)
    if text_length % 2 > 0:
        return text[(text_length // 2)]
    return ""


def mid_2(text):
    return text[(len(text) // 2)] if len(text) % 2 > 0 else ""


if __name__ == "__main__":
    print(mid("python3"))    # output: h
    print(mid_2("python3"))  # output: h
