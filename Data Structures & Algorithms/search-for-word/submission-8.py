class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        def dfs(i,j,w):
            if w == len(word):
                return True    
            if i == ROWS or j == COLS or i < 0 or j < 0 or (i,j) in path or board[i][j] != word[w]:
                return False
            
            path.add((i,j))
            res = (dfs(i+1, j, w+1) or dfs(i, j+1, w+1) or dfs(i-1, j, w+1) or dfs(i, j-1, w+1))
            path.remove((i,j))
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False
