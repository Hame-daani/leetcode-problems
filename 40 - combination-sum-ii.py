# https://leetcode.com/problems/combination-sum-ii/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        O(2^N)
        """

        def helper(candidates, chosed, target):
            if target == 0:
                yield chosed
                return
            if target < 0:
                return
            i = 0
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                yield from helper(
                    candidates[i + 1 :],
                    chosed + [candidates[i]],
                    target - candidates[i],
                )

        return list(helper(sorted(candidates), [], target))


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
