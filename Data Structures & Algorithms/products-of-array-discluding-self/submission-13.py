class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preArr = []
        postArr = []
        val = 1
        for i in range(len(nums)):
            preArr.append(val)
            val *= nums[i]
        
        val2 = 1
        for i in range(len(nums) - 1, -1, -1):
            postArr.append(val2)
            val2 *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(preArr[i] * postArr[len(nums) - i - 1])
        return res

