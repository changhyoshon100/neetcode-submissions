class Solution:
    def floodFill(
        self, image: List[List[int]],
        sr: int, sc: int, color: int
    ) -> List[List[int]]:
        original = image[sr][sc]
        rows, cols = len(image), len(image[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            visited.add((row, col))
            image[row][col] = color

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and image[nr][nc] == original
                    and (nr, nc) not in visited
                ):
                    dfs(nr, nc)

        dfs(sr, sc)
        return image