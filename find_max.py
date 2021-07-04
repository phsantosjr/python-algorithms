from utils import timer_decorator


def find_max_1(array: list) -> int:
    """

    O(n^2)

    :param array: list of integers
    :return: integer
    """
    overallmax = array[0]
    for i in array:
        is_greatest = True
        for j in array:
            if j > i:
                is_greatest = False
        if is_greatest:
            overallmax = i
    return overallmax


def find_max_2(array: list) -> list:
    """

    Best Case:
    Worst Case: O(n)

    :param array: list of integers
    :return: integer
    """
    max_so_far = array[0]
    for i in array:
        if i > max_so_far:
            max_so_far = i
    return max_so_far