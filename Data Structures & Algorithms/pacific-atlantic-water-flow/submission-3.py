class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        bucket_pac = set()
        bucket_atl = set()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0:
                    pac.add((r,c))
                if c == 0:
                    pac.add((r,c))
                if r == ROWS - 1:
                    atl.add((r,c))
                if c == COLS - 1:
                    atl.add((r,c))
        
        def dfs(r,c,ht,prev,bucket):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or ht < prev or (r,c) in bucket:
                return 
            
            bucket.add((r,c))
            
            dfs(r+1,c,heights[max(0,min(r+1,ROWS-1))][c],ht,bucket)
            dfs(r-1,c,heights[max(0,min(r-1,ROWS-1))][c],ht,bucket)
            dfs(r,c+1,heights[r][max(0,min(c+1,COLS-1))],ht,bucket)
            dfs(r,c-1,heights[r][max(0,min(c-1,COLS-1))],ht,bucket)
        
        for r,c in pac:
            dfs(r,c,heights[r][c],0, bucket_pac)
        
        for r,c in atl:
            dfs(r,c,heights[r][c],0, bucket_atl)
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in bucket_atl and (r,c) in bucket_pac:
                    res.append((r,c))
        return res


