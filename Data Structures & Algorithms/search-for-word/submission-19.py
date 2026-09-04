class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        arr = []
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    arr.append((r,c))
        path = set()
        def dfs(r,c,w):
            if w == word:
                return True
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return False
            if (r,c) in path:
                return False
            w = w + board[r][c]
            
            path.add((r,c))
            res = (
                dfs(r + 1, c, w) or 
                dfs(r - 1, c, w) or 
                dfs(r, c + 1, w) or 
                dfs(r, c - 1, w)
            )
            path.remove((r,c))
            return res
        ans = False
        for a in arr:
            r,c = a
            ans = ans or dfs(r,c,"")
        return ans

