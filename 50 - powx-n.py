# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base, exp: int):
            """
            Exponentitation by squaring
            source: https://en.wikipedia.org/wiki/Exponentiation_by_squaring
            """
            if exp == 0:
                return 1
            if exp == 1:
                return base
            if (exp & 1) != 0:
                # if the last 'bit' is set, then it's an odd number
                # 3 & 1 = 0011 & 0001
                # 4 & 1 = 0100 & 0001
                return base * helper(base * base, exp // 2)
            else:
                return helper(base * base, exp // 2)

        sign = n < 0
        n = abs(n)
        s = helper(x, n)
        return 1 / s if sign else s


print(Solution().myPow(2.0000, 10))
