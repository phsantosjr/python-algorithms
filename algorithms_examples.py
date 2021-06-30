def sum_numbers_loop(n: int) -> int:
    """
    BIG-O Notation = O(n)
    """
    result = 0
    for i in range(n + 1):
        result += i
    return result


def sum_numbers(n: int) -> float:
    """
    BIG-O Notation = O(3)
    """
    return (n * (n + 1)) / 2


def bubble_sort(array: list) -> list:
    """
    BIG-O Notation = O(n**2)
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


def swap(m: int, n: int, arr: list):
    arr[m], arr[n] = arr[n], arr[m]


def print_star_line(size=20):
    print(size * "*")


if __name__ == "__main__":
    print_star_line()
    print("Testing sum_numbers with 10")
    print(sum_numbers(10))
    print_star_line()
    print("Testing sum_numbers_loop with 10")
    print(sum_numbers_loop(10))
    print_star_line()
    print("Testing bubble_sort with [8,5,2,9,5,6,3]")
    print(bubble_sort([8,5,2,9,5,6,3]))
    print_star_line()


