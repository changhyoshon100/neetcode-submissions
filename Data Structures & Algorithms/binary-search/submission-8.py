class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1: return 0
        L, R = 0, len(nums) - 1
        res = -1
        while L <= R:
            mid = (L + R) // 2 
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] < target:
                L = mid + 1
            else: 
                R = mid -1
            
        return res 