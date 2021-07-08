from utils import timer_decorator

"""
The following function prints the powers of 2 from 1 through n (inclusive). For example, if n is 4, it would
print 1, 2, and 4.

"""


@timer_decorator
def power_of_two(n: int) -> int:
    """

    BIG-O = O(log n)

    :param n:
    :return:
    """
    if n < 1:
        return 0

    elif n == 1:
        return 1

    else:
        prev = power_of_two(n // 2)
        return prev * 2
