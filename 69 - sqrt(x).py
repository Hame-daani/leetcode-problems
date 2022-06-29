# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, n: int) -> int:
        """
        binary search: O(log n)
        """
        low = 0
        high = n
        while low <= high:
            mid = (low + high) // 2
            if n > mid * mid:
                low = mid + 1
            elif n < mid * mid:
                high = mid - 1
            else:
                return mid
        return high


print(Solution().mySqrt(6))
