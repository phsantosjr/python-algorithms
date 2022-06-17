def decode(num: int) -> str:
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    for letter, n in zip(roman, nums):
        result += letter * int(num / n)
        num %= n
    return result


def main():
    print("Convert 1 to I : ", decode(1))
    print("Convert 2 to II : ", decode(2))
    print("Convert 5 to V : ", decode(2))
    print("Convert 150 to CL : ", decode(150))


if __name__ == "__main__":
    main()
