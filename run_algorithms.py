from utils import print_star_line
from tower_of_hanoi import tower_of_hanoi
from palindrome import *
from two_number_sum import two_number_sum
from find_min import find_min_1, find_min_2
from find_max import find_max_1, find_max_2
from smallest_difference import smallest_difference_1, smallest_difference_2


for i in range(1, 4):
    print(f'Testing Tower Of Hanoi for {i} disks')
    tower_of_hanoi(i)
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

print("Testing palindrome_5 with 'dog ma i am god', 'dog am i am god'")
print(palindrome_5('dog ma i am god', 'dog am i am god'))
print_star_line()

print("Testing palindrome_6 with 'apple','pleap'")
print(palindrome_6('apple', 'pleap'))
print_star_line()

print("Testing two_number_sum with [3, 5, -4, 8, 11, 1, -1, 6], 10")
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
print_star_line()

print("Testing find_min_1 with [5, 8, 4, 3, 1]")
print(find_min_1([5, 8, 4, 3, 1]))
print_star_line()

print("Testing find_min_2 with [5, 8, 4, 3, 1]")
print(find_min_2([5, 8, 4, 3, 1]))
print_star_line()

print("Testing find_max_1 with [5, 8, 4, 3, 1]")
print(find_max_1([5, 8, 4, 3, 1]))
print_star_line()

print("Testing find_max_2 with [5, 8, 4, 3, 1]")
print(find_max_2([5, 8, 4, 3, 1]))
print_star_line()

print("Testing smallest_difference_1 with [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]")
print(smallest_difference_1([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
print_star_line()

print("Testing smallest_difference_2 with [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]")
print(smallest_difference_2([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
print_star_line()
