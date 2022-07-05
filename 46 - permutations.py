# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        O(N*N!): time
        O(N!): space
        """

        def helper(candidates, chosed):
            if not candidates:
                yield chosed
            for i in range(len(candidates)):
                yield from helper(
                    candidates[:i] + candidates[i + 1 :], chosed + [candidates[i]]
                )

        return list(helper(nums, []))


print(Solution().permute([1, 2, 3]))
