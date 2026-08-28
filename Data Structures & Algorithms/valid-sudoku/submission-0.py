class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        for i in range(ROWS):
            row_c = set()
            col_c = set()
            grid_c = set()

            for j in range(COLS):
                
                if board[i][j] in row_c or board[j][i] in col_c or board[(i // 3)*3 + (j // 3)][(i%3)*3 + (j % 3)] in grid_c:
                    return False
                if board[i][j] != '.':
                    row_c.add(board[i][j])
                if board[j][i] != '.':
                    col_c.add(board[j][i])
                if board[(i // 3)*3 + (j // 3)][(i%3)*3 + (j % 3)] != '.':
                    grid_c.add(board[(i // 3)*3 + (j // 3)][(i%3)*3 + (j % 3)])
        return True
            

