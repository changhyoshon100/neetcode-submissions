class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        edges = []
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS - 1 or r == 0 or c == COLS - 1 or c == 0:
                    if board[r][c] == "O":
                        edges.append((r,c))
        
        edge_coor = set()
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in edge_coor or board[r][c] == 'X':
                return
            
            edge_coor.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r,c in edges:
            dfs(r,c)

        edge_coor = list(edge_coor)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in edge_coor:
                    board[r][c] = 'X'
        