# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # return self.general_way(matrix)
        return self.pythonic_way(matrix)

    def general_way(self, matrix):
        """
        O(M): time: M number of rows
        O(1): space
        """
        n = len(matrix)
        for i in range(n // 2 + 1):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = (
                    matrix[~j][i],
                    matrix[i][j],
                    matrix[j][~i],
                    matrix[~i][~j],
                )

    def pythonic_way(self, matrix):
        """
        O(N): time
        O(N): space
        """
        matrix[:] = map(list, zip(*matrix[::-1]))


matrix = [[(i + 1) + 5 * j for i in range(5)] for j in range(5)]
Solution().rotate(matrix)
print(*matrix, sep="\n")
