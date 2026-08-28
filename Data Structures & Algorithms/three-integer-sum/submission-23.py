class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums)):
            value = nums[i]
            L,R = i+1, len(nums) - 1
            while L < R:
                if value + nums[L] + nums[R] == 0:
                    res.add(tuple([value,nums[L],nums[R]]))
                    L += 1
                    R -= 1
                elif value + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    R -= 1
        return list(res)
                    

