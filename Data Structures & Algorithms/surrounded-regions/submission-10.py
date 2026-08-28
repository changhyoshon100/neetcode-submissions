class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        border = set()
        visit = set()
        for r in range(ROWS):
            if board[r][COLS - 1] == 'O':
                border.add((r,COLS - 1))
            if  board[r][0] == 'O':
                border.add((r,0))
        
        for c in range(COLS):
            if board[0][c] == 'O':
                border.add((0,c))
            if board[ROWS - 1][c] == 'O':
                border.add((ROWS - 1, c))
        
        def dfs(r,c,board):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            dfs(r+1,c,board)
            dfs(r-1,c,board)
            dfs(r,c+1,board)
            dfs(r,c-1,board)

        
        for r,c in list(border):
            dfs(r,c,board)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                else:
                    continue
        

