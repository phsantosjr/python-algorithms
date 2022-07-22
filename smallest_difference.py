from utils import timer_decorator


"""
Time Complexity = O(nlong(n) + mlog(m))
"""


@timer_decorator
def smallest_difference_1(array_one: list, array_two: list) -> list:
    if not array_one or not array_two:
        raise Exception("Array can not be empty")

    array_one = sorted(array_one)
    array_two = sorted(array_two)
    index_one = 0
    index_two = 0
    smallest_diff = float("inf")
    result_pair = []

    while index_one < len(array_one) and index_two < len(array_two):
        first_num = array_one[index_one]
        second_num = array_two[index_two]

        current_diff = abs(first_num - second_num)

        if current_diff < smallest_diff:
            smallest_diff = current_diff
            result_pair = [first_num, second_num]

        if first_num <= second_num:
            index_one += 1
        else:
            index_two += 1

    return result_pair


"""
Complexity O(n**2)
"""


@timer_decorator
def smallest_difference_2(array_one: list, array_two: list) -> list:
    if not array_one or not array_two:
        raise Exception("Array can not be empty")

    array_one = sorted(array_one)
    array_two = sorted(array_two)
    smallest_diff = float("inf")

    for i in range(len(array_one)):
        for j in range(len(array_two)):
            if abs(array_one[i] - array_two[j]) < smallest_diff:
                diff = abs(array_one[i] - array_two[j])
                m, n = i, j
    return [array_one[m], array_two[n]]
