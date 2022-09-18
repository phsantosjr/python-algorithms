from utils import timer_decorator


@timer_decorator
def prefix_average_1(array: list) -> list:
    """

    BIG-O Notation: O(n^2)

    :param array: list of integers
    :return: list of averages
    """
    n = len(array)
    a = [0] * n

    for j in range(n):
        total = 0

        for i in range(j + 1):
            total += array[i]
        a[j] = total / (j + 1)
    return a


@timer_decorator
def prefix_average_2(array: list) -> list:
    """

    BIG-O Notation: O(n^2)

    :param array: list of integers
    :return: list of averages
    """
    n = len(array)
    A = [0] * n

    for j in range(n):
        A[j] = sum(array[0:j+1]) / (j + 1)

        """
        Asymptotically, this implementation is no better. Even though the expression, 
        sum(S[0:j+1]), seems like a single command, it is a function call and
        an evaluation of that function takes O( j + 1) time in this context. Technically, the
        computation of the slice, S[0:j+1], also uses O( j + 1) time, as it constructs a new
        list instance for storage.
        """

    return A


@timer_decorator
def prefix_average_3(array: list) -> list:
    """

    BIG-O Notation: O(n)

    :param array: list of integers
    :return: list of averages
    """
    n = len(array)
    a = [0] * n
    total = 0

    for j in range(n):
        total += array[j]
        a[j] = total / (j + 1)

    return a
