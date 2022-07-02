# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        O(1)
        """
        row_seen = [[] for _ in range(9)]
        col_seen = [[] for _ in range(9)]
        box_seen = [[] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                v = board[row][col]
                if v != ".":
                    row_seen[row].append(v)
                    col_seen[col].append(v)
                    box_seen[(row // 3) * 3 + col // 3].append(v)
        if any(len(set(row)) < len(row) for row in row_seen):
            return False
        if any(len(set(col)) < len(col) for col in col_seen):
            return False
        if any(len(set(box)) < len(box) for box in box_seen):
            return False
        return True


board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]
print(Solution().isValidSudoku(board))
