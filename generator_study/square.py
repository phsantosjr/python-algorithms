MAX = 5


def fetch_squares(max_root):
    """ Normal way to create a function, without generators """
    squares = []
    for n in range(max_root):
        squares.append(n**2)
    return squares


def gen_squares(max_num):
    """ Using generators """
    for num in range(max_num):
        yield num ** 2


def main():
    print(20*'*')
    print('Square without Generator\n')
    for square in fetch_squares(MAX):
        print(fetch_squares(square))

    print(20 * '*')
    print('Square with Generator')
    for square in gen_squares(MAX):
        print(square)


if __name__ == "__main__":
    main()
