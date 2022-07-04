# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        for c in num1:
            n1 = n1 * 10 + int(c)
        n2 = 0
        for c in num2:
            n2 = n2 * 10 + int(c)
        s = n1 * n2
        if not s:
            return "0"
        res = ""
        while s:
            res = str(s % 10) + res
            s = s // 10
        return res
