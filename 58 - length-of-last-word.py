# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return self.general_way(s)
        return self.pythonic_way(s)

    def general_way(self, s):
        """
        faster o(k) k: length of the last word
        """
        l = 0
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        while s[i] != " " and i >= 0:
            l += 1
            i -= 1
        return l

    def pythonic_way(self, s):
        """
        slower o(n) n: length of the whole s
        """
        return len(s.split()[-1])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
