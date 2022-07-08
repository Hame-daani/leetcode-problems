# https://leetcode.com/problems/minimum-path-sum/

from math import inf
from functools import lru_cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.recursive(grid)
        # return self.dynamic(grid)

    def recursive(self, grid):
        """
        O(M*N): time: too slow, didn't pass the time limit test
        O(M*N): space: for cache
        """
        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def helper(i, j, s):
            curr = grid[i][j]
            if i == m - 1 and j == n - 1:
                return s + curr

            down = helper(i + 1, j, s + curr) if i < m - 1 else inf
            right = helper(i, j + 1, s + curr) if j < n - 1 else inf
            return min(down, right)

        return helper(0, 0, 0)

    def dynamic(self, grid):
        """
        O(M*N): time
        O(1): space
        """
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if i and j:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i:
                    # first row
                    grid[i][j] += grid[i - 1][j]
                elif j:
                    # first column
                    grid[i][j] += grid[i][j - 1]
        return grid[-1][-1]


# inp = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# inp = [[1, 2, 3], [4, 5, 6]]

inp = [
    [7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
    [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
    [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
    [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
    [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
    [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
    [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
    [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
    [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
    [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
    [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
    [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9],
]

print(Solution().minPathSum(inp))
