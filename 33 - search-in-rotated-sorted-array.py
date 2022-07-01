# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, low, high, target):
            """
            O(log n)
            """
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                # low is ok
                if nums[low] <= target < nums[mid]:
                    return helper(nums, low, mid - 1, target)
                else:
                    return helper(nums, mid + 1, high, target)
            else:
                # low is not ok!
                if nums[mid] < target <= nums[high]:
                    return helper(nums, mid + 1, high, target)
                else:
                    return helper(nums, low, mid - 1, target)

        return helper(nums, 0, len(nums) - 1, target)


# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
# print(Solution().search([5, 1, 3], 5))
print(Solution().search([1, 2, 3, 4, 5], 4))
