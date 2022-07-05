# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        O(N*log N)
        O(N)
        """
        intervals.sort()
        start = 0
        end = 1
        output = []
        while end <= len(intervals):
            max_end = intervals[start][1]
            while end < len(intervals) and max_end >= intervals[end][0]:
                max_end = max(max_end, intervals[end][1])
                end += 1
            output.append([intervals[start][0], max(intervals[start][1], max_end)])
            start = end
            end += 1
        return output


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# print(Solution().merge([[1, 4], [0, 2], [3, 5]]))
