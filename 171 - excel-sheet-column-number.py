# https://leetcode.com/problems/excel-sheet-column-number/


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        O(N)
        """
        s = 0
        for c in columnTitle:
            s = s * 26 + (ord(c) - 65 + 1)
        return s


print(Solution().titleToNumber("ZY"))
