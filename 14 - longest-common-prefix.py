# https://leetcode.com/problems/longest-common-prefix/

from typing import List
from itertools import takewhile


def allsame(x):
    return len(set(x)) == 1


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # takewhile: Make an iterator that returns elements from the iterable as long as the predicate is true.
        # zip: will stops as soon as one of them is finished
        r = [i[0] for i in takewhile(allsame, zip(*strs))]
        return "".join(r)


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
