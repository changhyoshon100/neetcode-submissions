class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, buttom = 0, len(matrix) - 1
        row = float('inf')
        while top <= buttom:
            mid = (top + buttom) // 2
            
            if matrix[mid-1][-1] < target and matrix[mid][-1] >= target:
                row = mid
                break
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                buttom = mid - 1

            # if mid == 0:
            #     row = mid
            #     break
            
        L, R = 0, len(matrix[0]) - 1
        # print(row)
        if row == float('inf'):
            row = 0
        while L <= R:
            mid = (L + R) // 2
            if matrix[row][mid] < target:
                L = mid + 1
            elif matrix[row][mid] > target:
                R = mid - 1
            else:
                return True
        return False 