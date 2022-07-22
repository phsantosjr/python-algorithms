from utils import timer_decorator


@timer_decorator
def sum_product(array: list) -> dict:
    """

    BIG-O Notation: This will take O(N) time. The fact that we iterate through the array twice doesn't matter.

    :param array: list of numbers
    :return:
    """
    total_sum = 0
    total_product = 1

    for i in array:
        total_sum += i

    for i in array:
        total_product *= i

    return {"sum": total_sum, "product": total_product}
