"""
The sum of any number from a array should be such that it equals the target number.

Time complexity = O(n)

"""

from utils import timer_decorator


def two_number_sum(array: list, target_sum: int) -> list:
    for n in array:
        residual = target_sum - n
        if residual in array and residual != n:
            return sorted([residual, n])
    return []
