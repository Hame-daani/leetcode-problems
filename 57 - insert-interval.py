# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        O(N): time
        O(N): space
        """
        index = 0
        while index < len(intervals) and intervals[index][0] < newInterval[0]:
            index += 1
        intervals.insert(index, newInterval)
        # same as #56 problem
        output = []
        for curr in intervals:
            if not output or output[-1][1] < curr[0]:
                output.append(curr)
            else:
                output[-1][1] = max(output[-1][1], curr[1])
        return output


print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
