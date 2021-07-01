import timeit


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


def palindrome_1(word_1: str, word_2: str) -> bool:
    umalista = list(word_2)

    pos1 = 0
    aindaOK = True

    while pos1 < len(word_1) and aindaOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(umalista) and not encontrado:
            if word_1[pos1] == umalista[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1

        if encontrado:
            umalista[pos2] = None
        else:
            aindaOK = False

        pos1 = pos1 + 1

    return aindaOK


def palindrome_2(word_1: str) -> bool:
    return word_1[::-1] == word_1


def palindrome_3(word: str) -> bool:
    reversed_string = ""
    for i in reversed(range(len(word))):
        reversed_string += word[i]
    return word == reversed_string


def palindrome_4(word: str, i=0) -> bool:
    """
    BIG-O Notation = O(n^2)
    """
    j = len(word) - 1 - i
    if i > j:
        return True
    else:
        return word[i] == word[j] and palindrome_4(word, i + 1)


def even_or_odd(value: int) -> bool:
    """
    BIG-O Notation = O(1)
    """
    return value % 2 == 0


def fact(n: int) -> int:
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


def fact2(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fact2(n-1)


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
    print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))
    print_star_line()

    print("Testing insertion_sort( with [8,5,2,9,5,6,3]")
    print(insertion_sort([8, 5, 2, 9, 5, 6, 3]))
    print_star_line()

    print("Testing selection_sort( with [8,5,2,9,5,6,3]")
    print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
    print_star_line()

    print("Testing palindrome_1 with 'abcd', 'dcba'")
    print(palindrome_1('abcd', 'dcba'))
    print_star_line()

    print("Testing palindrome_2 with 'radar'")
    print(palindrome_2('radar'))
    print_star_line()

    print("Testing palindrome_3 with 'ana'")
    print(palindrome_3('ana'))
    print_star_line()

    print("Testing palindrome_4 with 'dogmaiamgod'")
    print(palindrome_4('dogmaiamgod'))
    print_star_line()

    print("Testing even_or_odd with 2")
    print(even_or_odd(2))
    print_star_line()

    print("Testing even_or_odd with 3")
    print(even_or_odd(3))
    print_star_line()

    print("Testing fact with 3")
    print(fact(3))
    print_star_line()

    print("Testing fact2 with 3")
    print(fact2(3))
    print_star_line()
