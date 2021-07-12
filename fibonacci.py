from utils import timer_decorator
from math import sqrt


def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


def fibonacci_1(n: int):
    a = 1
    b = 1
    if n == 1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b =a
            a = total
            print(total)


@timer_decorator
def fibonacci_2(start_number: int, end_number: int):
    n = 0
    cur = F(n)
    while cur <= end_number:
        if start_number <= cur:
            print(cur)
        n += 1
        cur = F(n)


@timer_decorator
def fibonacci_3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
