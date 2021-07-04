from utils import timer_decorator


@timer_decorator
def palindrome_1(word_1: str, word_2: str) -> bool:
    """

    As 𝑛 gets large, the 𝑛2 term will dominate the 𝑛 term and the 12 can be ignored. Therefore, this solution is 𝑂(𝑛2).

    :param word_1: word
    :param word_2: word
    :return:
    """
    word_array = list(word_2)

    pos1 = 0
    still_ok = True

    if len(word_1) != len(word_2):
        return False

    while pos1 < len(word_1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(word_array) and not found:
            if word_1[pos1] == word_array[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            word_array[pos2] = None
        else:
            still_ok = False

        pos1 = pos1 + 1

    return still_ok


@timer_decorator
def palindrome_2(word_1: str) -> bool:
    return word_1[::-1] == word_1


@timer_decorator
def palindrome_3(word: str) -> bool:
    reversed_string = ""
    for i in reversed(range(len(word))):
        reversed_string += word[i]
    return word == reversed_string


@timer_decorator
def palindrome_4(word: str, i=0) -> bool:
    """
    BIG-O Notation = O(n^2)
    """
    j = len(word) - 1 - i
    if i > j:
        return True
    else:
        return word[i] == word[j] and palindrome_4(word, i + 1)


@timer_decorator
def palindrome_5(word_1: str, word_2: str) -> bool:
    """

    O(n^2)

    :param word_1:
    :param word_2:
    :return: if is or not a palindrome
    """
    word_1_list = list(word_1)
    word_2_list = list(word_2)

    word_1_list.sort()
    word_2_list.sort()

    pos = 0
    matches = True

    while pos < len(word_1) and matches:
        if word_1_list[pos] == word_2_list[pos]:
            pos += 1
        else:
            matches = False

    return matches


@timer_decorator
def palindrome_6(word_1: str, word_2: str) -> bool:
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(word_1)):
        pos = ord(word_1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(word_2)):
        pos = ord(word_2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True

    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK
