class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, buttom = 0, ROWS - 1
        mid = -1
        while top <= buttom:
            mid = (top + buttom) // 2
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                break 
            elif matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][-1] > target:
                buttom = mid - 1
        
        if mid == -1: return False
        
        left, right = 0, COLS - 1
        while left <= right:
            c = (left + right) // 2
            
            if matrix[mid][c] < target:
                left = c + 1
            elif matrix[mid][c] > target:
                right = c - 1
            else:
                return True
        return False
            
            