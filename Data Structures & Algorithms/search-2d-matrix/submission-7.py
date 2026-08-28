class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        L = 0
        R = len(matrix)-1
        if target > matrix[len(matrix)-1][-1] or target < matrix[0][0]:
            return False
        if target == matrix[0][-1] or target == matrix[len(matrix)-1][-1]:
            return True
        print(L,R)
        if len(matrix) >= 2:
            
            while L <= R:
                mid = (L+R) // 2
                # print(mid, target, matrix[mid][-1])
                if target == matrix[mid][-1]:
                    return True
                elif target < matrix[mid][-1]:
                    R = mid - 1
                elif target > matrix[mid][-1]:
                    L = mid + 1
        L_ = 0
        R_ = len(matrix[L]) - 1
        
        while L_ <= R_:
            mid_ = (L_+R_) // 2
            if matrix[L][mid_] == target:
                return True
            elif matrix[L][mid_] > target:
                R_ = mid_ - 1
            else:
                L_ = mid_ + 1
        return False



            
            