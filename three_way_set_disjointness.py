from utils import timer_decorator


@timer_decorator
def disjoint_1(array_one: list, array_two: list, array_three: list) -> bool:
    """

    BIG-O Notation: O(n^3)

    :param array_one: list of item
    :param array_two: list of item
    :param array_three:  list of item
    :return: bool
    """
    for a in array_one:
        for b in array_two:
            for c in array_three:
                if a == b == c:
                    return False

    return True


@timer_decorator
def disjoint_2(array_one: list, array_two: list, array_three: list) -> bool:
    """

    BIG-O Notation: O(n^3)

    :param array_one: list of item
    :param array_two: list of item
    :param array_three:  list of item
    :return: bool
    """
    for a in array_one:
        for b in array_two:
            if a == b:
                for c in array_three:
                    if a == c:
                        return False

    return True
