# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""
def solution(B) -> list:
    total_patrols = 0
    total_submarines = 0
    total_destroyers = 0
    ship = "#"
    empty = "."

    board_width = len(B[0])
    board_height = len(B)
    position_checked = []

    pos_height = 0

    for pos_width in range(board_height):
        for pos_height in range(board_width):
            if (pos_width, pos_height) in position_checked:
                continue

            if B[pos_width][pos_height] == ship:
                # check board to right
                is_ship_mark = True
                pos_width_2 = pos_width + 1
                found_w = 0
                while pos_width_2 < board_height:
                    if B[pos_width_2][pos_height] == ship:
                        found_w += 1
                    pos_width_2 += 1

                # check board to bottom
                pos_height_2 = pos_height + 1
                found_h = 0
                while pos_height_2 < board_width:
                    if B[pos_width][pos_height_2] == ship:
                        found_h += 1
                    pos_height_2 += 1

                # check board to up
                if pos_height > 0:
                    pos_height_2 = pos_height - 1
                    while pos_height_2 > 0:
                        if B[pos_width][pos_height_2] == ship:
                            found_h += 1
                        pos_height_2 -= 1

                if (found_w == 0) and (found_h == 0):
                    total_patrols += 1

                if (found_w == 2) and (found_h == 2):
                    total_submarines += 1

            position_checked.append((pos_width, pos_height))

    return [total_patrols, total_submarines, total_destroyers]


print(solution(['.#..#', '##..#', '...#.']))

"""


def solution(n):
    d = [0] * 30
    l = 0

    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1

    for p in range(1, 1 + l):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1


def main():
    print(solution(10000000))


if __name__ == "__main__":
    main()

