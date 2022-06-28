# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # general way (kadane algorithm) (faster) # #
        #
        curr = maximum = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            maximum = max(curr, maximum)
        return maximum
        #
        # # divide and conquer (slower) # #
        #
        # return self.dc(nums, 0, len(nums) - 1)

    def dc(self, nums, low, high):
        if low > high:
            return 0
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        curr = 0
        left_cross = -100000000000
        # HACK we iterate 'reversed' cause we want to calculate subarray consisting of 'mid' point itself.
        for n in reversed(nums[low:mid]):
            curr = curr + n
            left_cross = max(curr, left_cross)

        curr = 0
        right_cross = -100000000000
        for n in nums[mid : high + 1]:
            curr = curr + n
            right_cross = max(curr, right_cross)

        cross_sum = max(left_cross, right_cross, (left_cross + right_cross))
        left_sum = self.dc(nums, low, mid)
        right_sum = self.dc(nums, mid + 1, high)
        return max(cross_sum, left_sum, right_sum)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
