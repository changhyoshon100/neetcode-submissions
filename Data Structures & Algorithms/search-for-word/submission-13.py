class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        origin = []
        ROWS = len(board)
        COLS = len(board[0])

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    origin.append((i,j))
        
        def dfs(row, col, w, path, i):
            if i == len(word): return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False
            
            if word[i] != board[row][col]:
                return False
            if (row, col) in path:
                return False
            
            path.add((row,col))

            res = (dfs(row + 1, col, w, path, i + 1) or
            dfs(row, col + 1, w, path, i + 1) or
            dfs(row - 1, col, w, path, i + 1) or
            dfs(row, col - 1, w, path, i + 1))

            path.remove((row, col))
            return res
            
        res = False
        for r,c in origin:
            res = res or dfs(r,c,"",set(),0)
        return res