# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        O(N * M log M): time: M log M for sorting each word of M length
        O(N): space
        """
        anagrams = {}
        for s in strs:
            w = "".join(sorted(s))
            try:
                anagrams[w].append(s)
            except:
                anagrams[w] = [s]
        return list(anagrams.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
