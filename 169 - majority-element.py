# https://leetcode.com/problems/majority-element/

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return self.first(nums)
        return self.second(nums)

    def first(self, nums):
        """
        O(N): time
        O(N): space
        """
        counter = {}
        for n in nums:
            try:
                counter[n] += 1
            except:
                counter[n] = 1
        return max(counter.keys(), key=lambda x: counter[x])

    def second(self, nums):
        """
        O(N): time
        O(1): space
        """
        major = None
        count = 0
        for n in nums:
            if count == 0:
                major = n
            if major == n:
                count += 1
            else:
                count -= 1
        return major
