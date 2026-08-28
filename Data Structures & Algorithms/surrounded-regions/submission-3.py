class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        circle = []
        
        visit = set()
        inner = set()
        for r in range(ROWS):
            if board[r][0] == 'O':
                visit.add((r,0))
            if board[r][COLS - 1] == 'O':
                visit.add((r,COLS - 1))

        for c in range(COLS):
            if board[0][c] == 'O' and (r,c) not in visit:
                visit.add((0,c))
            if board[ROWS - 1][c] == 'O' and (r,c) not in visit:
                visit.add((ROWS - 1,c))
        print(visit)
                
        
        def dfs(r,c,prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X' or (r,c) in inner:
                return
            print(r,c)
            if prev[r][c] == 'O':
                inner.add((r,c))
            
            dfs(r+1,c,prev)
            dfs(r-1,c,prev)
            dfs(r,c+1,prev)
            dfs(r,c-1,prev)
        for r,c in list(visit):
            dfs(r,c,board)
        print(inner, visit)
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS - 1 or c == COLS - 1 or r == 0 or c == 0:
                    continue
                if (r,c) not in inner:
                    board[r][c] = 'X'
                
        
        
