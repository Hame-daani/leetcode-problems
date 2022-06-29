# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2 or len(s) < 2:
            return s
        rev = False
        row = col = 0
        out = [[" " for _ in range(len(s) // 2 + 1)] for _ in range(numRows)]
        for k in range(len(s)):
            out[row][col] = s[k]
            if row == numRows - 1:
                rev = True
            elif rev and row == 0:
                rev = False
            if rev:
                row -= 1
                col += 1
            else:
                row += 1
        return "".join(a for b in out for a in b if a != " ")


print(Solution().convert("ABC", 2))
