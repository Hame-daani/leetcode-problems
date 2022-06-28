# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #
        # # general way # #
        #
        n = len(haystack)
        for curr in range(n):
            i = curr
            j = 0
            while i < n and j < len(needle):
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    break
            if j == len(needle):
                break
        if j == len(needle):
            return i - j
        else:
            return -1
        #
        # # pythonic way ##
        #
        # try:
        #     return haystack.index(needle)
        # except:
        #     return -1


print(Solution().strStr("mississippi", "issip"))
