from utils import swap


def bubble_sort(array: list) -> list:
    """ BIG-O Notation = O(n^2) """

    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i+1, array)
                is_sorted = False
        counter += 1
    return array
