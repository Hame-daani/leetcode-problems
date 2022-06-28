# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # return self.general_way(digits)
        return self.pythonic_way(digits)

    def general_way(self, digits):
        """
        slower
        """
        if digits[-1] == 9:
            if len(digits) == 1:
                # [9] + 1
                return [1, 0]
            else:
                # [1,2,9]+1 = [1,3,0]
                return self.general_way(digits[:-1]) + [0]
        else:
            # i < 9
            digits[-1] += 1
        return digits

    def pythonic_way(self, digits):
        """
        faster
        """
        num = int("".join(map(str, digits)))
        num += 1
        return [int(d) for d in str(num)]


print(Solution().plusOne([1, 2, 9]))
