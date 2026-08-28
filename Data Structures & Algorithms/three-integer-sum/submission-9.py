class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i,v in enumerate(nums):
            L = i+1
            R = len(nums) - 1
            while L < R:
                if nums[L] + nums[R] + v < 0:
                    L += 1
                elif nums[L] + nums[R] + v > 0:
                    R -= 1
                else:
                    if [v,nums[L],nums[R]] not in res:
                        res.append([v,nums[L],nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        
        return res

