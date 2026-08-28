class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)-1
        COLS = len(matrix[0])-1
        
        top, bot = 0, ROWS
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top += 1
            elif target < matrix[mid][0]:
                bot -= 1
            else:
                break

        if top > bot:
            return False

        row = (top+bot)//2
        L, R = 0, COLS

        while L <= R:
            mid = (L + R) // 2
            if target > matrix[row][mid]:
                L = mid + 1
            elif target < matrix[row][mid]:
                R = mid - 1
            else:
                return True
        return False

