# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            s = str(x)[::-1][:-1]
        else:
            s = str(x)[::-1]
        r = int(s)
        return 0 if r > 2**31 else r * sign
