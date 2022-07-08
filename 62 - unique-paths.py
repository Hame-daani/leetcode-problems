# https://leetcode.com/problems/unique-paths/


from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.recursive(m, n)
        # return self.dynamic(m, n)

    def recursive(self, m, n):
        """
        O(M*N): time
        O(M*N): space: for cache

        top-down approach with cache
        """

        @lru_cache(maxsize=m * n)
        def helper(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            down = helper(i + 1, j) if i < m - 1 else 0
            right = helper(i, j + 1) if j < n - 1 else 0
            return down + right

        return helper(0, 0)

    def dynamic(self, m, n):
        """
        O(M*N): time
        O(N): space: only the last row

        bottom-up approach.
        """
        # index '0' is the last cell
        row = [1] * n
        # from the first column, there's only one path always
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]


print(Solution().uniquePaths(10, 10))
