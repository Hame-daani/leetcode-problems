# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        val = self.countAndSay(n - 1)
        substrings = [[val[0]]]
        index = 0
        for i in range(1, len(val)):
            if val[i] != substrings[index][0]:
                substrings.append([val[i]])
                index += 1
            else:
                substrings[index].append(val[i])
        res = ""
        for s in substrings:
            res += f"{len(s)}{s[0]}"
        return res


print(Solution().countAndSay(5))
