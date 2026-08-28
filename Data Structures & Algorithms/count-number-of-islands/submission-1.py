class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        def search(self, r, c,grid):
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
                
            if grid[r][c] == '0':
                return 
            elif grid[r][c] == '1':
                grid[r][c] = '0'
                search(self,r+1,c,grid)
                search(self,r-1,c,grid)
                search(self,r,c+1,grid)
                search(self,r,c-1,grid)
                return 1
            
        
        for r in range(rows):
            for c in range(cols):
                if search(self,r,c,grid) == 1:
                    ans += 1
        # print(grid[0][1])
        return ans
                    
        

