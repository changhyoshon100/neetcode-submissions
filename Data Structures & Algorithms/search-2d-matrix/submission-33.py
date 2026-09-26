class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row * col - 1

        while left <= right:
            mid = left + (right - left) // 2
            result = matrix[mid // col][mid % col]

            if result < target:
                left = mid + 1
            elif result > target:
                right = mid - 1
            else:
                return True

        return False