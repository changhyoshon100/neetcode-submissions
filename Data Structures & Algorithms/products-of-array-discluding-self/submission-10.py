class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        
        for i in range(len(nums)):
            x = 1
            for j in range(i+1, len(nums)):
                x *= nums[j]
            for k in range(i):
                x *= nums[k]
            arr.append(x)
        return arr