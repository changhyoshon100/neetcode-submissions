class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if grid[r][c] == '0' or (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    cnt += 1
                    dfs(r, c)

        return cnt