# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        O(log n + log n)
        """

        def helper(nums, low, high, t):
            """
            O(log n)
            """
            if low >= high:
                return low
            mid = (low + high) // 2
            if t > nums[mid]:
                return helper(nums, mid + 1, high, t)
            else:
                return helper(nums, low, mid, t)

        low = helper(nums, 0, len(nums), target)
        # find the possible index of next number
        high = helper(nums, 0, len(nums), target + 1)
        # the index before is the answer
        high -= 1
        if low <= high:
            return [low, high]
        else:
            return [-1, -1]


print(Solution().searchRange([5, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10], 8))
