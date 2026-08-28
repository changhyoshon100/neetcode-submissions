class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else: return -1
        res = float('infinity')
        L, R = 0, len(nums) - 1
        
        while L < R:
            mid = (L + R) // 2
            print(res, L, R, mid)
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
            res = min(res, R)
        print(res)
        arr1 = nums[:res]
        arr2 = nums[res:]
        print(arr1, arr2, res)
        flag = False
        def search_(arr):
            L, R = 0, len(arr) - 1
            while L <= R:
                mid = (L + R) // 2
                if arr[mid] > target:
                    R = mid - 1
                elif arr[mid] < target:
                    L = mid + 1
                else: 
                    # print(res, mid)
                    return mid
            return -1
        
        a = search_(arr1) 
        b = search_(arr2)
        if a == -1 and b == -1: return -1
        ans = a + b
        
        if a == -1: return res + b
        else: return a
