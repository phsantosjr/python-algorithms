from utils import print_star_line, timer_decorator


def bubble_sort(array: list) -> list:
    """
    BIG-O Notation = O(n^2)
    """

    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) -1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i+1, array)
                is_sorted = False
        counter += 1
    return array


def insertion_sort(array: list) -> list:
    """
    BIG-O Notation = O(n^2)
    """

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array


def selection_sort(array: list) -> list:
    """
    BIG-O Notation = O(n^2)
    """
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


def swap(m: int, n: int, arr: list):
    arr[m], arr[n] = arr[n], arr[m]


def even_or_odd(value: int) -> bool:
    """
    BIG-O Notation = O(1)
    """
    return value % 2 == 0


if __name__ == "__main__":
    print_star_line()

    print("Testing bubble_sort with [8,5,2,9,5,6,3]")
    print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))
    print_star_line()

    print("Testing insertion_sort( with [8,5,2,9,5,6,3]")
    print(insertion_sort([8, 5, 2, 9, 5, 6, 3]))
    print_star_line()

    print("Testing selection_sort( with [8,5,2,9,5,6,3]")
    print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
    print_star_line()

    print("Testing even_or_odd with 2")
    print(even_or_odd(2))
    print_star_line()

    print("Testing even_or_odd with 3")
    print(even_or_odd(3))
    print_star_line()


