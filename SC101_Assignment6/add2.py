"""
File: add2.py
Name: Alan
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    cur1 = l1
    cur2 = l2
    if cur1.val + cur2.val > 9:
        ans = ListNode(cur1.val + cur2.val - 10, None)
        ans.next = ListNode(1, None)
    else:
        ans = ListNode(cur1.val + cur2.val, None)
        # ans.next = ListNode(0, None)
    # cur1 = cur1.next
    # cur2 = cur2.next
    # cur_ans = ans
    # cur_ans.next = ans.next

    # while cur1 or cur2 is not None:
    #     if cur1 is None and cur2 is not None:
    #         cur_ans.next = ListNode(cur_ans.val + cur2.val, cur2.next)
    #         cur2 = cur2.next
    #         cur_ans = cur_ans.next
    #     elif cur1 is not None and cur2 is None:
    #         cur_ans.next = ListNode(cur_ans.val + cur1.val, cur1.next)
    #         cur1 = cur1.next
    #         cur_ans = cur_ans.next
    #     elif cur1 is not None and cur2 is not None:
    #         if cur1.val + cur2.val > 9:
    #             cur_ans.next = ListNode(cur_ans.val + cur1.val + cur2.val - 10, None)
    #             cur_ans.next.next = ListNode(1, None)
    #             cur1 = cur1.next
    #             cur2 = cur2.next
    #             cur_ans = cur_ans.next
    #         else:
    #             cur_ans.next = ListNode(cur_ans.val + cur1.val + cur2.val, None)  # ans.next.val may > 9
    #             cur1 = cur1.next
    #             cur2 = cur2.next
    #             cur_ans = cur_ans.next
    #     else:
    #         pass
    #
    # if cur_ans.val > 9:
    #     cur_ans.val -= 10
    #     cur_ans.next = ListNode(1, None)  # carry
    while cur1.next or cur2.next is not None:  # obob
        if
    return ans


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
