# https://leetcode.com/problems/subsets-ii/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(n, l, out=None):
            if out is None:
                out = []
            if n == 0:
                return [out]
            i = l[0]
            x = helper(n - 1, l[1:], out + [i])
            l = list(filter(lambda x: x != i, l))
            return x + helper(len(l), l, out)

        return helper(len(nums), nums)


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
