class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def is_safe(row, col, val):
            # checking valid column
            for r in range(ROWS):
                if r != row and val == board[r][col]:
                    return False

            # checking valid row
            for c in range(COLS):
                if c != col and val == board[row][c]:
                    return False

            # checking valid sub-grid
            sub_row = row - row % 3
            sub_col = col - col % 3
            for r in range(3):
                for c in range(3):
                    if board[r+sub_row][c+sub_col] == val and r+sub_row != row and c+sub_col != col:
                        return False

            return True

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != '.' and not is_safe(r, c, board[r][c]):
                    return False
        return True
