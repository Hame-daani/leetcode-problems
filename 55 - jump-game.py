# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        O(N): time
        O(1): space
        """
        furtherest = 0
        end = len(nums) - 1
        for curr in range(len(nums)):
            if curr > furtherest:
                return False
            furtherest = max(furtherest, curr + nums[curr])
            if furtherest >= end:
                return True
        return True


print(Solution().canJump([3, 2, 1, 0, 4]))
