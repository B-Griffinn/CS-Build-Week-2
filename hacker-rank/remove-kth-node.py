#
# Complete the 'removeKthLinkedListNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def removeKthLinkedListNode(head, k):
    list_length = 1

    cur = head
    temp = head

    # while we have not reached the end of our list...
    while cur.next is not None:

        # increment our counter variable by 1
        list_length += 1

        # incrememnt our cur pointer to the next value in order to keep loop moving forward
        cur = cur.next

        # check if he length of our list is longer that the element given + 1 to ensure we can delete that node
        if list_length > k + 1:
            # if true, move our temp variable pointer up one
            temp = temp.next

    # if the length of our list == k exactly then we simply return our head.next value
    if list_length == k:
        return head.next

    # otherwise move our temp pointer two places and return the head
    else:
        temp.next = temp.next.next
        return head
