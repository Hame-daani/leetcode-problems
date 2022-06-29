from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        left = 0
        right = len(height) - 1
        vmax = 0
        while left < right:
            m = min(height[left], height[right])
            vmax = max(vmax, m * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return vmax


print(Solution().maxArea([1, 2, 1]))
