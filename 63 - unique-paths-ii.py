# https://leetcode.com/problems/unique-paths-ii/

from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        O(M*N): time
        O(M*N): space: for cache

        top-down approach with cache
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @lru_cache(maxsize=m * n)
        def helper(i, j):
            if obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            down = helper(i + 1, j) if i < m - 1 else 0
            right = helper(i, j + 1) if j < n - 1 else 0
            return down + right

        return helper(0, 0)
