class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        upLeft = 0
        downLeft = len(matrix) - 1
        print(upLeft, downLeft)
        
        while upLeft <= downLeft:
            mid = (upLeft + downLeft) // 2
            
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                upLeft = mid + 1
            else:
                downLeft = mid - 1
        
        # print(mid-1)
        # print(upLeft,matrix[mid][0])
        # print(downLeft,matrix[mid][0])
        i,j = 0,len(matrix[mid-1]) - 1
        if matrix[mid][0] > target:
            while i <= j:
                mid_col = (i + j) // 2
                if target == matrix[mid-1][mid_col]:
                    return True
                elif target >= matrix[mid-1][mid_col]:
                    i = mid_col + 1
                else:
                    j = mid_col - 1
            return False
        else:
            while i <= j:
                mid_col = (i + j) // 2
                if target == matrix[mid][mid_col]:
                    return True
                elif target >= matrix[mid][mid_col]:
                    i = mid_col + 1
                else:
                    j = mid_col - 1
            return False


