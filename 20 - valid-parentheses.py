# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            try:
                if c == "(":
                    stack.append("p")
                elif c == "[":
                    stack.append("b")
                elif c == "{":
                    stack.append("m")
                elif c == ")" and stack.pop() != "p":
                    return False
                elif c == "]" and stack.pop() != "b":
                    return False
                elif c == "}" and stack.pop() != "m":
                    return False
            except:
                return False
        return len(stack) == 0


print(Solution().isValid("([]([])})"))
