class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = len(matrix) - 1, 0
        print(up,down)
        R = 0
        

        while down <= up:
            row = (up + down) // 2
            if matrix[row-1][-1] < target and matrix[row][-1] > target:
                print('row', row)
                R = row
                break
            elif matrix[row][-1] < target:
                print('row2', row)
                down = row + 1
            elif matrix[row-1][-1] > target:
                print('row3', row)
                up = row - 1
            else:
                return True
            

        left, right = 0,  len(matrix[R]) - 1
        print(R)
        while left <= right:
        
            mid = (left + right) // 2
            print(R, mid)
            if matrix[R][mid] < target:
                left = mid + 1
            elif matrix[R][mid] > target:
                right = mid - 1
            else:
                print('mid', mid)
                return True
        return False
        

                
            


