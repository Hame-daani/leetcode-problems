# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        O(N^(target/min))
        """

        def helper(candidates, chosed, target):
            if target == 0:
                yield chosed
                return
            if target < 0:
                return
            for i in range(len(candidates)):
                yield from helper(
                    candidates[i:], chosed + [candidates[i]], target - candidates[i]
                )

        return list(helper(candidates, [], target))


print(Solution().combinationSum([2, 3, 6, 7], 7))
