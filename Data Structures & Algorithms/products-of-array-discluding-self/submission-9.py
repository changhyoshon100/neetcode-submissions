class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        value = 1
        for i in range(len(nums)):
            prefix.append(value)
            value *= nums[i]
        
        value = 1
        for i in range(len(nums)-1,-1,-1):
            postfix.append(value)
            value *= nums[i]
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * postfix[len(nums) - i - 1])
        return ans
