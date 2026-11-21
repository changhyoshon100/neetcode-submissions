class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postArr = []
        preArr = []
        val = 1
        for i in range(len(nums)):
            preArr.append(val)
            val *= nums[i]
        val = 1
        for i in range(len(nums) - 1, -1, -1):
            postArr.append(val)
            val *= nums[i]
        
        res = []
        for i in range(len(postArr)):
            res.append(preArr[i] * postArr[len(nums) - i - 1])
        return res


                    
