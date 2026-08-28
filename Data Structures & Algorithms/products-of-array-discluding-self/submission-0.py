class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = [0] * len(nums)
        prefix[0] = postfix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, 0, -1):
            postfix[i-1] = postfix[i] * nums[i]
        
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        return res
            

