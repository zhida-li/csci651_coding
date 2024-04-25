"""
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/

"""

import collections

class Solution:
    def isValidSudoku(self, board):
        # Initialize default dictionaries to track the numbers in each row, column, and square.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    # Skip empty cells.
                    continue
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    # If the number is already in the current row, column, or square, return False.
                    return False
                
                # Add the number to the row, column, and square.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # If no duplicates are found, return True.
        return True

# Example usage:
# Create a Sudoku puzzle with some cells filled in.
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Create an intentionally invalid Sudoku puzzle with a repeated number in the first row.
invalid_board = [
    ["5", "3", "3", ".", "7", ".", ".", ".", "."],  # '3' is repeated here, making it invalid.
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Check if the current board is valid.
is_valid = Solution().isValidSudoku(board)
print(f"The board is valid or not: {is_valid}")
is_valid = Solution().isValidSudoku(invalid_board)
print(f"The board is valid or not: {is_valid}")