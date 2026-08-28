class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        arr.append(1)
        val = 1
        for i in range(len(nums)-1):
            val = val * nums[i]
            arr.append(val)
        arr2 = []
        arr2.append(1)
        val2 = 1
        for i in range(len(nums)-1,0,-1):
            val2 = val2 * nums[i]
            arr2.append(val2)

        
        res = []
        for i in range(len(nums)):
            res.append(arr[i] * arr2[len(nums) - i - 1])
        return res

