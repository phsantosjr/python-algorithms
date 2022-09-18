"""

"""

# First Solution
# Source: https://www.youtube.com/watch?v=s7AvT7cGdSo
from typing import List
from itertools import permutations


def permute_v1(nums: List[int]) -> List[List[int]]:
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute_v1(nums)

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)

    return sorted(result)


# Second Solution
# using itertools permutations

def permute_v2(nums: List[int]) -> list:
    nums = ''.join(str(n) for n in nums)
    result = [[int(d) for d in i] for i in permutations(nums, len(nums))]
    return result


def main():
    list_int = [1, 2, 3]
    print(" Running v1")
    print(permute_v1(list_int))

    print(" Running v2")
    print(permute_v2(list_int))


if __name__ == "__main__":
    main()
