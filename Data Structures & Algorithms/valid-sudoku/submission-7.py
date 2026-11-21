class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            row = set()
            col = set()
            grid = set()
            for c in range(9):
                g_r = c // 3 + (r // 3) * 3
                g_c = c % 3 + (r % 3) * 3
                
                if board[c][r] != "." and board[c][r] in col:
                    return False
                if board[r][c] != "." and board[r][c] in row:
                    return False
                if board[g_r][g_c] != "." and board[g_r][g_c] in grid:
                    return False

                row.add(board[r][c])
                col.add(board[c][r])
                grid.add(board[g_r][g_c])
        return True