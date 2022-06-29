# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        # remove whitespace
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0
        # sign
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            sign = 1
            i += 1
        # conversion
        start = i
        while i < len(s) and s[i].isnumeric():
            i += 1
        if s[start:i].isnumeric():
            r = int(s[start:i])
        else:
            return 0
        if r >= 2**31:
            if sign == 1:
                r = 2**31 - 1
            if sign == -1:
                r = 2**31
        return r * sign


print(Solution().myAtoi("2147483648"))
