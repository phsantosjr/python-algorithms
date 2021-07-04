from utils import timer_decorator


@timer_decorator
def find_min_1(array: list) -> int:
    """

    O(n^2)

    :param array: list of integers
    :return: integer
    """
    overallmin = array[0]
    for i in array:
        is_smallest = True
        for j in array:
            if i > j:
                is_smallest = False
        if is_smallest:
            overallmin = i
    return overallmin


@timer_decorator
def find_min_2(array: list) -> list:
    """

    Best Case:
    Worst Case: O(n)

    :param array: list of integers
    :return: integer
    """
    min_so_far = array[0]
    for i in array:
        if i < min_so_far:
            min_so_far = i
    return min_so_far
