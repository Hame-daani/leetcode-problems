# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(self.general_way(int(a), int(b)))
        # return self.pythonic_way(a, b)

    def general_way(self, a, b, carry=0):
        """
        faster
        """
        if not (a or b):
            return carry
        r = (a % 10) + (b % 10) + carry
        carry = r // 2
        r = r % 2
        return self.general_way(a // 10, b // 10, carry) * 10 + r

    def pythonic_way(self, a, b):
        """
        kinda slower
        """
        return str(bin(int(a, 2) + int(b, 2)))[2:]


print(Solution().addBinary("1111", "1111"))
