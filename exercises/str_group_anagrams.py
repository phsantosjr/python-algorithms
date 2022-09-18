"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Leetcode: https://leetcode.com/problems/group-anagrams/



"""
from collections import defaultdict
from typing import List


def solution_1(words: List[str]) -> List[List[str]]:
    """
    Source: https://www.youtube.com/watch?v=vzdNOK2oB2E&ab_channel=NeetCode
    """
    res = defaultdict(list)
    for s in words:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()


def solution_2(words: List[str]) -> List[List[str]]:
    """

    Source: https://leetcode.com/problems/group-anagrams/discuss/19202/5-line-Python-solution-easy-to-understand
    """
    letters_to_words = defaultdict(list)
    for word in words:
        letters_to_words[tuple(sorted(word))].append(word)
    return list(letters_to_words.values())


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(10*"*")
    print("Running solution_1")
    print(solution_1(strs))

    print(10 * "*")
    print("Running solution_2")
    print(solution_2(strs))


if __name__ == "__main__":
    main()