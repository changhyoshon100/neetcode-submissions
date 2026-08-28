class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            if nums[mid] < nums[R]:
                R = mid
            else:
                L = mid + 1
        pivot = L
        
        def sep(arr, pv):
            return [arr[:pv], arr[pv:]]
        
        f_arr, sec_arr = sep(nums, pivot)
        def findTarget(arr, target):
            L, R = 0, len(arr) - 1
            while L <= R:
                
                mid = (L + R) // 2

                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            return -1
        findFst = findTarget(f_arr, target)
        findSec = findTarget(sec_arr, target)
        if max(findFst, findSec) == -1:
            return -1
        if findFst == -1:
            return len(f_arr) + findSec
        else:
            return findFst
