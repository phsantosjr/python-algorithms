from utils import timer_decorator


@timer_decorator
def fact_1(n: int) -> int:
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


@timer_decorator
def fact_2(n: int) -> int:
    if n == 0:
        return 1
    return n * fact_2(n-1)
