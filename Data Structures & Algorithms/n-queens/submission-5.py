class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos = set()
        neg = set()
        board = [['.'] * n for _ in range(n)]
        res = []

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return res
            
            for c in range(n):
                if c in cols or (r + c) in pos or (r - c) in neg:
                    continue

                cols.add(c)     
                pos.add((r + c))    
                neg.add((r - c))    
                board[r][c] = 'Q'   
                dfs(r + 1)  

                cols.remove(c)
                pos.remove((r + c))
                neg.remove((r - c))
                board[r][c] = '.'
        dfs(0)
        return res


            