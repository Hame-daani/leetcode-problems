# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # # general way # #
        # #
        # i = 0
        # n = len(nums)
        # while i < n:
        #     if nums[i] == val:
        #         nums[i] = nums[n - 1]
        #         n -= 1
        #     else:
        #         i += 1
        # return n
        # #
        # # pythonc way (faster) # #
        nums.sort(key=lambda x: x != val, reverse=True)
        return len(nums) - nums.count(val)


nums = [0, 1, 2, 2, 3, 0, 4, 2]
n = Solution().removeElement(nums, 2)
print(n, nums)
