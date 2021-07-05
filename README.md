# Python Algorithms - Exercises #
![](https://img.shields.io/badge/Python-3.8-blue.svg)

The goal of this repository is to study BIG-O Notation, algorithm complexity, data structures, using some algorithms examples and exercises in Python.

We use a lot of sources for this project, have a look in these sources in last section of this README.

In python file you will find more than one version for the same algorithm. That's to show how can we improve performance for our codes.

### List of Algorithms ####

##### Sum #####

Is designed to sum numbers in :
- array
- sequence of number for o to number (n)

Python bult-in function to sum numbers in a iterable:
[Doc](https://docs.python.org/3/library/functions.html#sum)
```
sum(iterable)
```

##### Two Number Sum #####

Is designed to calculate the sum of two numbers giver a target number from an array.

##### Bubble Sort #####

##### Insertion Sort #####

##### Selection Sort #####

##### Palindrome ##### 
Source: [https://en.wikipedia.org/wiki/Palindrome]



##### Factorial ##### 
Source: [https://en.wikipedia.org/wiki/Factorial]

##### Tower of Hanoi #####
Source: [https://en.wikipedia.org/wiki/Tower_of_Hanoi]



##### Find Min #####
Is designed to find the minimum value in a array

##### Find Max #####
Is designed to find the maximum value in a array

##### Smallest Difference #####

Is designed to calculate the smallest difference from two arrays



### BIG-O Notation ####

>The big-Oh notation is used widely to characterize running times and space bounds
in terms of some parameter n, which varies from problem to problem, but is always
defined as a chosen measure of the “size” of the problem
>(Goodrich, Michael T., Data Structures and Algorithms in Python )

|Name | BIG O |
|---|---|
|Constant | O(c) |
|Linear | O(n) |
|Quadratic | O(n^2) |
|Cubic | O(n^3) |
|Exponential | O(2^n) |
|Logarithmic | O(log(n)) |
|Log Linear | O(nlog(n)) |


![](https://res.cloudinary.com/practicaldev/image/fetch/s--u5FI10Fg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/9f7ruqkkz9xl0937b1nf.png)


We illustrate the growth rates of the seven functions

|n | log n | n | n log n | n^2 | n^3| 2^n |
|---|---|---|---|---|---|---|
|8 | 3 | 8 | 24 | 64 | 512 | 256
|16 | 4 | 16 | 64 | 256 |  4.096 | 65.536
|32 | 5 | 32 | 160 | 1.024 | 32.768 | 4.294.967.296
|64 | 6 | 64 | 384 | 4.096 | 262.144 | 1.84 x 10^19
|128 | 7 | 128 | 896 | 16.384 | 2.097.152 | 3.40 x 10^38
|256 | 8 | 256 | 2.048 | 65.536 | 16.777.216 | 1.15 x 10^77
|512 | 9 | 512 | 4.608 | 262.144 | 134.217.728 | 1.34 x 10^154

Source: (Goodrich, Michael T., Data Structures and Algorithms in Python )


#### Constant Complexity ( O(c)) ####

The complexity of an algorithm is said be constant if the steps required to complete the execution of an algorithm remain constant.

```sum_numbers()```

#### Linear Complexity ( O(n)) ####


#### Quadratic Complexity ( O(n^2)) ####


#### Cubic Complexity ( O(n^2)) ####


### Sorting Algorithims Cheat Sheet ###

![](https://habrastorage.org/getpro/habr/post_images/4be/b00/dfb/4beb00dfb3cdb4f8665747189fa8910a.png)


### Data Structure Operations Cheat Sheet ###
![](https://jojozhuang.github.io/assets/images/uncategorized/9721/data_structure_operations.png)


### Recursion ###

> Any function wich calls itself is called recursive. A recursive method solves a problem by calling a copy of itself to work on a smaller problem. This is called the recursion step. The recursion can result in many more recursive calls.
It is important to ensure that the recursion terminates. Each time the function calls itself with a slightly simpler version of the original problem. The sequence of smaller problems must eventually converge on the base case. 
>(Karumanchi, Narasimha - Data Structure and Algorithmic Thinking with Python)

>In computing, recursion provides an elegant and powerful alternative for per-
forming repetitive tasks. In fact, a few programming languages (e.g., Scheme,
Smalltalk) do not explicitly support looping constructs and instead rely directly
on recursion to express repetition. Most modern programming languages support
functional recursion using the identical mechanism that is used to support tradi-
tional forms of function calls
>(Goodrich, Michael T., Data Structures and Algorithms in Python )


Examples of recursion:
- Factorial

```
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
```
- Fibonacci
- Tower of Hanoi
- Merge Sort, quick sort
- Binary search
- Divide and conquer algorithms

Source:
[https://realpython.com/python-thinking-recursively/]

### Sources ####

Introdução a notação Big-O para análise de algoritmos [https://www.youtube.com/watch?v=qEAZzi15Uck]

Python Basics and Algorithms Programming [https://www.amazon.com.br/gp/product/B09757C778/ref=ku_mi_rw_edp_ku]

Big O Notation and Algorithm Analysis with Python Examples[https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples]

Big-O Quizz[https://bigoquiz.com/]

PythonPro BR [https://github.com/pythonprobr/estrutura-de-dados]

Problem Solving with Algorithms and Data Structures using Python [https://runestone.academy/runestone/books/published/pythonds/index.html]

TheAlgorithms/Python [https://github.com/TheAlgorithms/Python]

Data Structures and Algorithms in Python [https://www.amazon.com.br/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275/]