from utils import timer_decorator


@timer_decorator
def method_1(array: list, k: int) -> int:
    if not array:
        return 0

    count = 0
    n = len(array)

    # Pick all elements one by one
    for i in range(0, n):

        # See if there is a pair of this picked element
        for j in range(i + 1, n):
            if array[i] - array[j] == k or array[j] - array[i] == k:
                count += 1

    return count


# Standard binary search function
def binary_search(arr: list, low: int, high: int, x: int) -> int:
    if high >= low:
        mid = low + (high - low) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binary_search(arr, (mid + 1), high, x)
        else:
            return binary_search(arr, low, (mid - 1), x)
    return -1


# Returns count of pairs with difference k in arr[] of size n.
def method_2(array: list, k: int) -> int:
    count = 0
    array = sorted(array)
    n = len(array)

    # code to remove
    # duplicates from arr[]

    # Pick a first element point
    for i in range(0, n - 1):
        if binary_search(array, i + 1, n - 1, array[i] + k) != -1:
            count += 1

    return count
