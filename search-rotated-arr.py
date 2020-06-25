"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""


def search(self, nums: List[int], target: int) -> int:

    storage = dict()

    if target not in nums:
        return -1

    if len(nums) <= 1:
        return 0

    if target is nums[0]:
        return 0

    for i in nums:

        if i not in storage:
            storage[i] = i

        return i
    return '###'
