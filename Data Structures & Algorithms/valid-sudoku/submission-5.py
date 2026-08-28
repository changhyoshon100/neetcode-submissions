class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row, col, grid = set(), set(), set()
            for j in range(9):
                gc = j % 3 + (i % 3) * 3
                gr = j // 3 + (i // 3) * 3
                
                if board[i][j] in row:
                    return False
                if board[i][j] != '.':
                    row.add(board[i][j])
                
                if board[j][i] in col:
                    return False
                if board[j][i] != '.':
                    col.add(board[j][i])

                if board[gr][gc] in grid:
                    return False
                if board[gr][gc] != '.':
                    grid.add(board[gr][gc])
                
        return True

