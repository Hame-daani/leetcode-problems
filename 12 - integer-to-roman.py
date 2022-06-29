# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ""
        numerals = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        for n in reversed(numerals):
            if num >= n:
                return numerals[n] + self.intToRoman(num - n)


print(Solution().intToRoman(3))
