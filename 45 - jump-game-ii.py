# https://leetcode.com/problems/jump-game-ii/

from functools import lru_cache
from math import inf
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        O(N): time
        O(1): space
        """
        furtherest = 0
        jump = 0
        steps = 0
        n = len(nums) - 1
        for i in range(n):
            # find furtherest index that we can reach
            furtherest = max(furtherest, i + nums[i])
            if i == jump:
                # only jump when we reach to our current jump
                # and jump to the furtherest that we can currently
                jump = furtherest
                steps += 1
            if jump == n:
                break
        return steps


print(Solution().jump([2, 3, 0, 1, 4]))
