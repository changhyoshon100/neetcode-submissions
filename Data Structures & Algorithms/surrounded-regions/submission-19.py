class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        edges = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == 'O':
                    edges.append((r,c))
                    visited.add((r,c))
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while edges:
            for i in range(len(edges)):
                r,c = edges.popleft()
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited or board[nr][nc] == 'X':
                        continue
                    edges.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited:
                    continue
                if board[r][c] == 'O':
                    board[r][c] = 'X'


                
                
            
