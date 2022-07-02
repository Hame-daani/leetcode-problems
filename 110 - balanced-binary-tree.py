# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        faster without cache :/
        for some reason...
        """

        def helper(root):
            if root is None:
                return 0
            return max(helper(root.left), helper(root.right)) + 1

        if root is None:
            return True
        return (
            abs(helper(root.left) - helper(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )
