class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        origin = []

        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS - 1 or r == 0 or c == COLS - 1 or c == 0:
                    if board[r][c] == 'O' and (r,c) not in origin:
                        origin.append((r,c))
        
        visited = set()
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X' or (r,c) in visited:
                return
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            

        for r,c in origin:
            dfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited:
                    board[r][c] = 'X'

