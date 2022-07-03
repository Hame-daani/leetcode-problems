# https://leetcode.com/problems/valid-palindrome/


import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.general_way(s)
        # return self.pythonic_way(s)

    def general_way(self, s: str):
        """
        O(N): slighty slower, less memory
        """
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

    def pythonic_way(self, s: str):
        """
        O(N): slighly faster, more memory
        """
        s = re.sub(r"[\W_]+", "", s).lower()
        return s == s[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
