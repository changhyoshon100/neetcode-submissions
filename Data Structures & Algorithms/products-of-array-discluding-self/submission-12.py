class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        x = 1
        for i in range(len(nums)):
            prefix.append(x)
            x *= nums[i]
        
        x = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix.append(x)
            x *= nums[i]
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * postfix[len(nums) - 1 - i])
        return ans