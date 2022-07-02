# https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        O(N^2)
        """
        res = []
        for row in range(1, numRows + 1):
            l = []
            for j in range(row):
                if j in (0, row - 1):
                    l.append(1)
                else:
                    l.append(res[row - 2][j - 1] + res[row - 2][j])
            res.append(l)
        return res


print(Solution().generate(10))
