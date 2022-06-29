# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maximum = ""
        for i in range(len(s)):
            # abba
            two_char = self.get_palindrome(s, i, i + 1)
            # aba
            one_char = self.get_palindrome(s, i, i)
            maximum = max([maximum, two_char, one_char], key=lambda x: len(x))
        return maximum

    def get_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]


print(Solution().longestPalindrome("cbbd"))
