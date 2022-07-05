# https://leetcode.com/problems/permutations-ii/

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        O(N*N!): time
        O(N!): space
        """

        def helper(candidates, chosed):
            if not candidates:
                yield chosed
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                yield from helper(
                    candidates[:i] + candidates[i + 1 :], chosed + [candidates[i]]
                )

        return list(helper(sorted(nums), []))


print(Solution().permuteUnique([1, 1, 2]))
