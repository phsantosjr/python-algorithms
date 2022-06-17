def decode(roman: str) -> int:
    roman = roman.upper()
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    val = 0
    roman_len = len(roman)

    for i in range(roman_len):
        if i > 0 and roman_dict.get(roman[i]) > roman_dict.get(roman[i - i]):
            val += roman_dict.get(roman[i]) - 2 * roman_dict.get(roman[i - i])
        else:
            val += roman_dict.get(roman[i])

    return val


def main():
    print("Convert I to 1 : ", decode("I"))
    print("Convert II to 2 : ", decode("II"))
    print("Convert V to 5 : ", decode("V"))


if __name__ == "__main__":
    main()

