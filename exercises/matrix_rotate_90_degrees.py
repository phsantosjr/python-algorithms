"""

Given a matrix n x n 2D representing an image, rotate the image in 90 degrees clockwise

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation

Source: https://www.youtube.com/watch?v=fMSJSS7eO1w&ab_channel=NeetCode

"""
from typing import List


def solution_1(matrix: List[List[int]]):
     l, r = 0, len(matrix) - 1

     while l < r:
         for i in range(r - l):
             top, bottom = l, r

             top_left = matrix[top][l + i]

             matrix[top][l + i] = matrix[bottom - i][l]

             matrix[bottom - i][l] = matrix[bottom][r - i]

             matrix[bottom][r - i] = matrix[top + i][r]

             matrix[top + i][r] = top_left

         r -= 1
         l += 1