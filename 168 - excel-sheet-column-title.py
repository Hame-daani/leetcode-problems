# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        i = columnNumber
        res = ""
        while i:
            if i % 26:
                res = chr(i % 26 + 64) + res
            else:
                res = chr(26 + 64) + res
                i -= 26
            i = i // 26
        return res


print(Solution().convertToTitle(52))
