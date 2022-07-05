# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # return self.general_way(matrix)
        return self.pythonic_way(matrix)

    def general_way(self, matrix):
        """
        O(N): somehow slower :/
        O(N): space
        """
        i_lower_bound = 0
        j_lower_bound = -1
        i_upper_bound = len(matrix) - 1
        j_upper_bound = len(matrix[0]) - 1
        i = j = 0
        i_step = 0
        j_step = 1
        output = []
        while (i_lower_bound <= i <= i_upper_bound) and (
            j_lower_bound <= j <= j_upper_bound
        ):
            output.append(matrix[i][j])
            if j == j_upper_bound and i == i_lower_bound:
                j_step = 0
                i_step = 1
                j_lower_bound += 1
            elif i == i_upper_bound and j == j_upper_bound:
                i_step = 0
                j_step = -1
                i_lower_bound += 1
            elif j == j_lower_bound and i == i_upper_bound:
                i_step = -1
                j_step = 0
                j_upper_bound -= 1
            elif i == i_lower_bound and j == j_lower_bound:
                i_step = 0
                j_step = 1
                i_upper_bound -= 1
            i += i_step
            j += j_step
        return output

    def pythonic_way(self, matrix):
        """
        O(N): somehow faster :/
        O(N): space: probably more!

        algorithm: **pop** the 'first row' then **transpose** the 'remaining matrix'.
        """
        return matrix and [*matrix.pop(0)] + self.pythonic_way([*zip(*matrix)][::-1])


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# matrix = [[3], [2]]
print(Solution().spiralOrder(matrix))
