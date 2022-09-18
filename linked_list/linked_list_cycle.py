"""


Leetcode: https://leetcode.com/problems/linked-list-cycle/
Source: https://www.youtube.com/watch?v=gBTe7lFR3vc

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():
    ...


if __name__ == '__main__':
    main()


