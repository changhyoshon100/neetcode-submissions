class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid 
            else:
                left = mid + 1
        pivot = left
        
        
        res = -2
        def binary(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1
        res1 = binary(nums[:pivot])
        res2 = binary(nums[pivot:])
        if res1 != -1:
            return res1
        if res2 != -1:
            return res2 + len(nums[:pivot])
        
        return -1
