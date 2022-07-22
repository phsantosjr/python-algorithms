from utils import swap


def selection_sort(array: list) -> list:
    """ BIG-O Notation = O(n^2) """
    i = 0
    while i < len(array):
        min_element = i
        j = i + 1
        while j < len(array):
            if array[min_element] > array[j]:
                min_element = j
            j += 1
        swap(i, min_element, array)
        i += 1
    return array
