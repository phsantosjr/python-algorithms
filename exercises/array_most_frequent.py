"""
Given an array what is the most frequently occurring element

"""
from collections import Counter
from typing import List, Union
from statistics import mode


def solution_1(items: List[Union[int, str]]) -> Union[int, str]:
    count = {}
    max_count = 0
    max_item = None

    for i in items:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    return max_item


def solution_2(items: List[Union[int, str]]) -> Union[int, str]:
    dict_response = {}
    count, itm = 0, ''
    for item in reversed(items):
        dict_response[item] = dict_response.get(item, 0) + 1
        if dict_response[item] >= count:
            count, itm = dict_response[item], item
    return itm


def solution_3(items: List[Union[int, str]]) -> Union[int, str]:
    counter = 0
    num = items[0]

    for i in items:
        curr_frequency = items.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


def solution_4(items: List[Union[int, str]]) -> Union[int, str]:
    return max(set(items), key=items.count)


def solution_5(items: List[Union[int, str]]) -> Union[int, str]:
    occurrence_count = Counter(items)
    return occurrence_count.most_common(1)[0][0]


def solution_6(items: List[Union[int, str]]) -> Union[int, str]:
    return mode(items)


def main():
    list_of_integers = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 10]
    print("Running solution 1 - array of ints")
    print(solution_1(list_of_integers))
    print("Running solution 2 - array of ints")
    print(solution_2(list_of_integers))
    print("Running solution 3 - array of ints")
    print(solution_3(list_of_integers))
    print("Running solution 4 - array of ints")
    print(solution_4(list_of_integers))
    print("Running solution 5 - array of ints")
    print(solution_5(list_of_integers))
    print("Running solution 6 - array of ints")
    print(solution_6(list_of_integers))

    list_of_strings = ['a', 'a', 'b', 'b', 'c', 'c', 'h2o', 'h2o', 'h2o', 'h2o']
    print("Running solution 1 - array of strings")
    print(solution_1(list_of_strings))
    print("Running solution 2 - array of strings")
    print(solution_2(list_of_strings))
    print("Running solution 3 - array of strings")
    print(solution_3(list_of_strings))
    print("Running solution 4 - array of strings")
    print(solution_4(list_of_strings))
    print("Running solution 5 - array of strings")
    print(solution_5(list_of_strings))
    print("Running solution 6 - array of strings")
    print(solution_6(list_of_strings))


if __name__ == "__main__":
    main()
