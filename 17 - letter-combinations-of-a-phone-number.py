# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List
from itertools import product


class Solution:
    letters = [
        [],
        [],
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"],
    ]

    def letterCombinations(self, digits: str) -> List[str]:
        # return self.pythonic_way(digits)
        return self.general_way(digits)

    def general_way(self, digits):
        """
        O(4^n): slightly faster
        """

        def helper(n, res):
            if n == len(digits):
                yield res
                return
            for c in self.letters[int(digits[n])]:
                yield from helper(n + 1, res + c)

        if len(digits) == 0:
            return []
        return list(helper(0, ""))

    def pythonic_way(self, digits):
        """
        O(4^n): max character is 4. 'n' is len of digits
        """
        if len(digits) == 0:
            return []
        nums = [self.letters[int(n)] for n in digits]
        return list(map("".join, product(*nums)))


print(Solution().letterCombinations("23"))
