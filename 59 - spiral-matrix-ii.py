# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # return self.general_way(n)
        return self.pythonic_way(n)

    def general_way(self, n: int):
        i_lower_bound = 0
        j_lower_bound = -1
        i_upper_bound = n - 1
        j_upper_bound = n - 1
        i = j = 0
        i_step = 0
        j_step = 1
        output = [[0 for _ in range(n)] for _ in range(n)]
        counter = 1
        while (i_lower_bound <= i <= i_upper_bound) and (
            j_lower_bound <= j <= j_upper_bound
        ):
            output[i][j] = counter
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
            counter += 1
        return output

    def pythonic_way(self, n: int):
        res, lo = [[n * n]], n * n
        while lo > 1:
            lo, hi = lo - len(res), lo
            res = [[*range(lo, hi)]] + [*map(list, zip(*res[::-1]))]
        return res


matrix = Solution().generateMatrix(4)
print(*matrix, sep="\n")
