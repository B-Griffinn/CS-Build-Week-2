"""

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""


def findDuplicate(self, nums: List[int]) -> int:

    # create a dict to store values that we have already visited
    storage = dict()

    # loop through the list
    for i in nums:

        # if we have already seen the number return that number
        if i in storage:
            return i

        # otherwise add to the dict and keep looping
        else:
            storage[i] = i
