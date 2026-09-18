class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        val = 0
        res = set()
        nums.sort()
        for i in range(len(nums)):
            val = nums[i]
            l,r = i+1, len(nums) - 1
            
            while l < r:
                add = nums[l] + nums[r] + val
                
                if add == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif add < 0:
                    l += 1
                else:
                    r -= 1
        return list(res)
                
