class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0: return max(nums)
        maximum = 0 
        res = []
        for i in range(len(nums)):
            # maximum = max(maximum, maximum + nums[i])
            maximum += nums[i]
            res.append(nums[i]) 
            if maximum < 0:
                maximum = 0
                res = []
        rm = 0
        arr = []
        for i in range(len(res)-1,-1,-1):
            rm += res[i]
            if rm > 0:
                continue

            if rm < 0:
                arr = res[:i]
                break
        if not arr: return sum(res)
        print(arr,maximum)
        return sum(arr) 