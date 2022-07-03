# https://leetcode.com/problems/single-number/

from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.general_way(nums)
        # return self.pythonic_way(nums)

    def general_way(self, nums):
        """
        O(N): time, slighty slower
        O(N): space
        """
        s = set(nums)
        return sum(s) * 2 - sum(nums)

    def pythonic_way(self, nums):
        """
        O(N): time, slighty faster
        O(1): space

        A xor B = S
        S xor B = A
        S xor A = B
        """
        return reduce(lambda a, b: a ^ b, nums)
