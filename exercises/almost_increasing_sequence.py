"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly
increasing sequence by removing no more than one element from the array.

SOURCE: CodeSignal

"""


def almost_increasing_sequence(sequence):
    dropped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if dropped:
                return False
            else:
                dropped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


if __name__ == "__main__":
    print(almost_increasing_sequence([1,2,3]))
