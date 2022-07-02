# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        O(N)
        """
        if root is None:
            return 0
        return (
            min(
                self.minDepth(root.left),
                self.minDepth(root.right),
                key=lambda x: x if x > 0 else inf,
            )
            + 1
        )
