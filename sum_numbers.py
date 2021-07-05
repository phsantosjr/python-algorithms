from utils import print_star_line, timer_decorator


@timer_decorator
def sum_numbers_loop(n: int) -> int:
    """
    BIG-O Notation = O(n)
    """
    result = 0
    for i in range(n + 1):
        result += i
    return result


@timer_decorator
def sum_numbers(n: int) -> float:
    """
    BIG-O Notation = O(c)
    """
    return (n * (n + 1)) / 2


@timer_decorator
def sum_numbers_in_list(array: list) -> int:
    """
    BIG-O Notation = O(n)
    """
    result = 0
    for i in array:
        result += i
    return result
