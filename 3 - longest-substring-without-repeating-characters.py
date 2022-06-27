# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store the last occurrence of a character
        chars = {}
        l = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            if c in chars:
                # if we found a repeated character, we start again from the next index of last occurence of this character
                start = max(start, chars[c] + 1)
            l = max(l, i - start + 1)
            chars[c] = i
        return l


s = Solution()
print(s.lengthOfLongestSubstring("aaaaaabcdaaaa"))
