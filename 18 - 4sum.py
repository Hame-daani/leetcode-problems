# https://leetcode.com/problems/4sum/

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        O(n^k-1): O(n^3) for '4sum'
        """

        def helper(nums, target, k):
            res = []
            if k == 2:
                low = 0
                high = len(nums) - 1
                while low < high:
                    s = nums[low] + nums[high]
                    if s > target or (
                        high < len(nums) - 1 and nums[high] == nums[high + 1]
                    ):
                        high -= 1
                    elif s < target or (low > 0 and nums[low] == nums[low - 1]):
                        low += 1
                    else:
                        res.append([nums[low], nums[high]])
                        low += 1
                        high -= 1
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    for r in helper(nums[i + 1 :], target - nums[i], k - 1):
                        res.append([nums[i]] + r)
            return res

        return helper(sorted(nums), target, 4)


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
