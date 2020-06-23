"""

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""


def containsDuplicate(self, nums: List[int]) -> bool:
    # we need a dict to store all our list nums
    storage = dict()

    # base case to ensure we are not given a lsit of 1 or an empty list
    if len(nums) <= 1:
        return False

    # loop through the list nums and assign each num to our dict
    for i in nums:

        # if our current index value is not already in our storage add it and append it to nodupes
        if i not in storage:
            # adding it
            storage[i] = i

        elif i in storage:
            return True
        else:
            return False
