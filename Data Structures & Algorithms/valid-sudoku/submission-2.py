class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9
        
        for i in range(SIZE):
            row, col, grid = set(), set(), set()
            for j in range(SIZE):
                g_j = (j % 3) + (i % 3) * 3
                g_i = (j // 3) + (i // 3) * 3
                if board[i][j] in row:
                    return False
                if board[i][j] != '.':
                    row.add(board[i][j])

                if board[j][i] in col:
                    return False
                if board[j][i] != '.' and board[j][i] not in col:
                    col.add(board[j][i])

                if board[g_i][g_j] in grid:
                    return False
                if board[g_i][g_j] != '.' and board[g_i][g_j] not in grid:
                    grid.add(board[g_i][g_j])
        return True
                
                 
