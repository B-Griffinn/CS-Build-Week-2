"""

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # base case ~> ensure the lists are not emptym if they are return the opposite sorted list
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # hold a dummy node in a double assigned variable in order to avoid overlooping as well as mutating during our loop which is not accepted in python
        dummy = temp = ListNode()
        # print(dummy)
        # print(temp)

        # while we have not reached the end of each linked list, loop thru
        while l1 is not None and l2 is not None:

            # if our current value at l1 is less that current value at l2...
            if l1.val < l2.val:

                # store our lesser value in a current var
                cur = l1

                # move the lesser list val pointer to the next varable in the LL
                l1 = l1.next

            # otherwise, ifour current value in l2 is less than current value in l1...
            else:

                # store the lesser value in l2 in a current var
                cur = l2

                # move the lessert list val pointer to the next variable in the LL
                l2 = l2.next

            # update our node AFTER we move to the next position
            temp.next = cur

            # move the temp in our new list node to be the next position
            temp = temp.next

        # assign the lesser value to the
        temp.next = l1 or l2

        # return our newly formed dummy node tail
        return dummy.next
