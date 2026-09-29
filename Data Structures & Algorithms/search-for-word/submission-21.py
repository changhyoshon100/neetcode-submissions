class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        keep = []
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    keep.append((r,c))

        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i]:
                
                return False
            if (r,c) in path: 
                return False
            

            path.add((r,c))
            ans = (dfs(r-1,c,i+1) or
            dfs(r+1,c,i+1) or
            dfs(r,c+1,i+1) or
            dfs(r,c-1,i+1))
            path.remove((r,c))
            return ans
        res = False
        for r,c in keep:
            res = res or dfs(r,c,0)
        return res