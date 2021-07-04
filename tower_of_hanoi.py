from utils import timer_decorator

recursive_calls_count = 0


def recursive_tower_of_hanoi(number_of_disks: int, origin: str, destiny: str, aux: str) -> None:
    """
    f(n) = 1 + 2 * f(n-1)
    f(n) = 1 + 2 * (1 + 2 * f(n-2)) -> 1 + 2 + 4*f(n-2)
    f(n) = 1 + 2 + 4 * ( 1 + 2 * f(n-3)) ->1 + 2 + 4 + 8* f(n-3)
    f(n) = 1 + 2 + 4 ... 2**(n-1)     (I)
    2 * f(n) = 2+ 4 + 8 ... 2 ** n    (II)
    f(n) = 2**n - 1                    II - I
    O(2**n) para tempo de execução
    O(n) para memória
    :param number_of_disks:
    :param origin:
    :param destiny:
    :param aux:
    :return:
    """
    global recursive_calls_count
    recursive_calls_count += 1
    if number_of_disks == 1:
        print(f'{origin} -> {destiny} : {number_of_disks}')
        return
    recursive_tower_of_hanoi(number_of_disks - 1, origin, aux, destiny)
    print(f'{origin} -> {destiny} : {number_of_disks}')
    recursive_tower_of_hanoi(number_of_disks - 1, aux, destiny, origin)


@timer_decorator
def tower_of_hanoi(number_of_disks: int):
    global recursive_calls_count
    recursive_calls_count = 0
    recursive_tower_of_hanoi(number_of_disks, origin='A', destiny='B', aux='C')