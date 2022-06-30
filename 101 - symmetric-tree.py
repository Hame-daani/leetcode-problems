# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(p, q):
            """
            O(n)
            """
            if p and q:
                return (
                    p.val == q.val
                    and helper(p.left, q.right)
                    and helper(p.right, q.left)
                )
            return p is q

        return helper(root.left, root.right)
