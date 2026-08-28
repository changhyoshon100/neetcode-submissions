class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curr, max_num = 0,0

        for i in range(len(nums)):
            curr = max(nums[i] + curr,0)
            max_num = max(curr, max_num)
            print(curr, max_num)
        if max_num == 0:
            for i in range(1,len(nums)):
                num = max(nums[0], nums[i])
            return num

        return max_num 
            
            


            