# https://leetcode.com/problems/climbing-stairs/
from functools import lru_cache


class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        return self.top_down(n)
        # return self.bottom_up(n)

    @lru_cache(None)
    def top_down(self, n):
        """
        O(n) but slower due to the function seting up
        """
        if n < 2:
            return 1
        return self.top_down(n - 1) + self.top_down(n - 2)

    def bottom_up(self, n):
        """
        O(n) but faster
        """
        if n < 2:
            return 1
        a = 1
        b = 2
        for i in range(2, n):
            a, b = b, a + b
        return b


print(Solution().climbStairs(38))
