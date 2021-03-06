"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
Example
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product.
Input/Output
[execution time limit] 4 seconds (py3)
[input] array.integer inputArray
An array of integers containing at least two elements.
Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.
[output] integer
The largest product of adjacent elements.

SOURCE: CodeSignal

"""


def adjacent_elements_product(inputArray):
    previous = inputArray[0]
    product = previous * inputArray[1]
    for i in inputArray[1::]:
        if previous * i > product:
            product = previous * i
        previous = i
    return product


if __name__ == "__main__":
    inputArray = [3, 6, -2, -5, 7, 3]
    print(adjacent_elements_product(inputArray))
