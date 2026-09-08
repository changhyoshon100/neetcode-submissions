class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edges = set()
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == 'O':
                    queue.append((r,c))
                    edges.add((r,c))
        
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in edges or board[nr][nc] != 'O':
                    continue
                queue.append((nr, nc))
                edges.add((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in edges:
                    board[r][c] = 'X'
        
        

        
                    
