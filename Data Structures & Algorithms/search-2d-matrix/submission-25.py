class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        R = 0
        while up <= down:
            mid = (up + down) // 2
            if matrix[mid-1][-1] < target and matrix[mid][-1] >= target:
                R = mid
                break
            elif matrix[mid][-1] < target:
                up = mid + 1
            else:
                down = mid - 1
        
        left, right = 0, len(matrix[R]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[R][mid] == target:    
                return True
            elif matrix[R][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
                