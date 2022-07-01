# https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def helper(a: str, s: int, b: int):
            """
            O(a/b)
            """
            if s > len(a):
                # it's not big enough for divison
                return ""
            # get a slice for divison operation
            rem = int(a[:s])
            # divison operatin
            n = 0
            while rem >= b:
                rem -= b
                n += 1
            # replace the slice with what remains after divison
            # also adding leading zero to maintain the whole length as it started
            a = f"{rem:0{s}}" + a[s:]
            # the final answer is n + divison of the next slice
            return str(n) + helper(a, s + 1, b)

        # XOR: if both negative, answer will be positive
        negative = (divisor < 0) ^ (dividend < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        n = helper(str(dividend), len(str(divisor)), divisor)
        n = int(n) if n else 0
        if negative:
            return min(2147483648, n) * -1
        else:
            return min(2147483647, n)


# print(Solution().divide(-2147483648, -1))
print(Solution().divide(33, 3))
