# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        O(N^2)
        O(rowIndex): space complexity
        """
        res = []
        for row in range(rowIndex + 1):
            l = []
            for j in range(row + 1):
                if j in (0, row):
                    l.append(1)
                else:
                    l.append(res[j - 1] + res[j])
            res = l
        return res


print(Solution().getRow(3))
