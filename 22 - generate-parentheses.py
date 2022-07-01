# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        O(4^n/sqrt(n))  :/
        """

        def helper(o, c):
            """
            o: as number of opened parantheses
            c: as number of closed parantheses
            """
            if not (o or c):
                yield ""
            if o:
                for r in helper(o - 1, c):
                    yield "(" + r
            if c and o < c:
                for r in helper(o, c - 1):
                    yield ")" + r

        return list(helper(n, n))


print(Solution().generateParenthesis(3))
