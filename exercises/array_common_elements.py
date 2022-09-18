"""

Common Elements in Two Sorted Arrays

return the common elements ( as an array ) between two sorted arrays of integers ( asceding order )

Example: The common elements between [1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10] are [1, 4, 9]

"""
from typing import List, Set


def solution_1(array_a: List[int], array_b: List[int]) -> List[int]:
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(array_a) and p2 < len(array_b):
        if array_a[p1] == array_b[p2]:
            result.append(array_a[p1])
            p1 += 1
            p2 += 2

        elif array_a[p1] > array_b[p2]:
            p2 += 1

        else:
            p1 += 1

    return result


def solution_2(array_a: List[int], array_b: List[int]) -> List[int]:
    """ Using set and intersection """
    a_set = set(array_a)
    b_set = set(array_b)

    if len(a_set.intersection(b_set)) > 0:
        return list(a_set.intersection(b_set))
    return []


def solution_3(array_a: List[int], array_b: List[int]) -> List[int]:
    """ Using list comprehension """
    return [i for i in array_a if i in array_b]


def main():
    print("Running solution 1")
    result = solution_1([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10])
    print(result)

    print("Running solution 2")
    result = solution_2([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10])
    print(result)

    print("Running solution 3")
    result = solution_3([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10])
    print(result)


if __name__ == '__main__':
    main()