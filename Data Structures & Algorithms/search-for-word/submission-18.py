class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r,c,res,i, path):
            if res == word:
                return True
            if len(res) > len(word) or r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r,c) in path:
                return False
            if word[i] != board[r][c]:
                return False
            path.add((r,c))
            res += board[r][c]
            
            a = (dfs(r+1,c,res,i+1, path) or
            dfs(r-1,c,res,i+1, path) or
            dfs(r,c+1,res,i+1, path) or
            dfs(r,c-1,res,i+1, path))
            path.remove((r,c))
            return a

        ans = False
        for r in range(len(board)):
            for c in range(len(board[0])):
                ans = ans or dfs(r,c,"",0,set())
        return ans