# https://leetcode.com/problems/3sum-closest/

from math import inf
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        O(n^2)
        """
        if len(nums) < 3:
            return []
        nums.sort()
        diff = inf
        maxsum = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    maxsum = s
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return maxsum
        return maxsum


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
