class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def valid(i,j,s):
            if board[i][j] == '.':
                return True
            return board[i][j] not in s
            
        for r in range(ROWS):
            row, col, grid = set(), set(), set()
            for c in range(COLS):
                g_r = (c // 3) + ((r // 3) * 3)
                g_c = (c % 3) + ((r % 3) * 3) 
                
                if not valid(r,c,row):
                    return False
                if board[r][c] != '.':
                    row.add(board[r][c])
                
                if not valid(c,r,col):
                    return False
                if board[c][r] != '.':
                    col.add(board[c][r])
                
                if not valid(g_r,g_c,grid):
                    return False
                if board[g_r][g_c] != '.':
                    grid.add(board[g_r][g_c])

        return True


                 
