class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):

            row = set()
            col = set()
            grid = set()
            for j in range(9):
                g_r = j // 3 + (i // 3) * 3
                g_c = j % 3 + (i % 3) * 3
                if board[i][j] != "." and board[i][j] in row:
                    return False
                if board[j][i] != "." and board[j][i] in col:
                    return False
                if board[g_r][g_c] != "." and board[g_r][g_c] in grid:
                    return False
                
                row.add(board[i][j])
                col.add(board[j][i])
                grid.add(board[g_r][g_c])
            
        return True



           
                