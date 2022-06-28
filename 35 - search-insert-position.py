# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = (end - start) // 2 + start
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        return start


print(Solution().searchInsert([1, 3, 5, 6], 5))
