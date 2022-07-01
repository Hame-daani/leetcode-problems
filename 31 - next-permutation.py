# https://leetcode.com/problems/next-permutation/

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        algorithm: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
        """
        # find the largest decreasing index
        k = len(nums) - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        if k < 0:
            # it's already the biggest permutation
            nums.sort()
            return
        # find the next index smaller than k
        l = len(nums) - 1
        while l > k and nums[k] >= nums[l]:
            l -= 1
        # swap k,l
        nums[k], nums[l] = nums[l], nums[k]
        # reverse nums[k+1:]
        nums[k + 1 :] = nums[:k:-1]


Solution().nextPermutation([1, 5, 8, 4, 7, 6, 5, 3, 1])
