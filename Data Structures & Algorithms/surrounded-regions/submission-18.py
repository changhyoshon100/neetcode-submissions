class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and ((r == 0 or r == ROWS - 1) or (c == 0 or c == COLS - 1)):
                    queue.append((r,c))
                    visit.add((r,c))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit or board[nr][nc] == "X":
                    continue
                
                visit.add((nr, nc))
                queue.append((nr,nc))
                
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit:
                    board[r][c] = "X"

            
        

