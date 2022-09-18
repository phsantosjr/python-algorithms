"""
Write a program to calculate how many prime numbers there are between 2 numbers

Given that the first param is less then second
"""
import sys


def is_prime_number(number: int) -> bool:
    if number in (0, 1):
        return True

    for i in range(2, int(number / 2) + 1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (number % i) == 0:
            return False

    return True


def main(first_number: int, second_number: int) -> None:
    acc = 0
    while first_number <= second_number:
        if is_prime_number(first_number):
            acc += 1

        first_number += 1

    print(f"There are {acc} prime numbers", file=sys.stderr)


if __name__ == '__main__':
    main(1, 10)
