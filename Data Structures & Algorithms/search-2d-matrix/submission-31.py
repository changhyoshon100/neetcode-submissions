class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, buttom = 0, len(matrix) - 1
        row = -1
        while top <= buttom:
            mid = (top + buttom) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                buttom = mid - 1
            else:
                top = mid + 1

        if row == -1: return False

        L, R = 0, len(matrix[0]) - 1
        while L <= R:
            mid = (L + R) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return False
