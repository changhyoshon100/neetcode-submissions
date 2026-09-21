class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def smallest(nums):
            L,R = 0, len(nums) - 1
            while L <= R:
                mid = (L + R) // 2
                if nums[mid] < nums[R]:
                    R = mid
                else:
                    L = mid + 1
            return R
        
        R = smallest(nums)
        arr1, arr2 = nums[:R], nums[R:]
        
        def binary(arr):
            L,R = 0, len(arr) - 1
            while L <= R:
                mid = (L + R) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            return -1
        idx1 = binary(arr1)
        idx2 = binary(arr2)
        
        if idx1 == -1 and idx2 != -1:
            return idx2 + len(arr1)
        elif idx2 == -1 and idx1 == -1:
            return -1
        else:
            return idx1
                
            