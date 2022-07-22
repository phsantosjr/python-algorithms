import functools
import time


def timer_decorator(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        if int(end - start) > 0:
            print(f"Run time for {func.__name__}: {(end - start):0.2f}s")
        else:
            print(f"Run time for {func.__name__}: {(end - start)*1000:0.2f}ms")
        return func(*args, **kwargs)

    return timer_wrapper


def print_star_line(size: int = 20) -> None:
    print(size * "*")


def swap(m: int, n: int, arr: list):
    arr[m], arr[n] = arr[n], arr[m]
