"""
The sum of any number from a array should be such that it equals the target number.

Time complexity = O(n)

"""
from typing import List


def two_number_sum(array: list, target_sum: int) -> list:
    for n in array:
        residual = target_sum - n
        if residual in array and residual != n:
            return sorted([residual, n])
    return []



"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution and you may not use same element twice

"""


def two_number_sum_2(array: List[int], target_sum: int) -> List[int]:
    prev_map = {}
    for i, n in enumerate(array):
        diff = target_sum - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []
