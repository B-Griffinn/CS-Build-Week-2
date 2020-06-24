"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # create a variable for our return statement which will be a new node entirely
        # initialize this new node with a value of 0, its /next will be none to begin with
        result = ListNode(0)

        # set the tail of our solution to be this new list node above
        tail = result

        # initialize a carrying variable for our left overs when we mod the result
        carrier = 0

        # loop through our l1 and l1 while we have not reached the end of the LLs
        while l1 is not None and l2 is not None:

            # catch case for LL == 0
            # return the other list only
            if l1.val == 0:
                return l2
            if l2.val == 0:
                return l1

            # check if our lists are empty
            if l1 is not None:
                value1 = l1.val
            elif l1 is None:
                value1 = 0

            if l2 is not None:
                value2 = l2.val
            elif l2 is None:
                value2 = 0

            carrier, out = divmod(value1 + value2 + carrier, 10)

            tail.next = ListNode(out)
            tail = tail.next

            if l1 is not None:
                l1 = l1.next
            else:
                l1 = None

            if l2 is not None:
                l2 = l2.next
            else:
                l2 = None

        return result.next
