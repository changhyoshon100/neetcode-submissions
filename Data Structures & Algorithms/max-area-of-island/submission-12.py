class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            curArea = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    curArea += dfs(nr, nc)

            return curArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea