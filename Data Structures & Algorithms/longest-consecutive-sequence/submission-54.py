class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = set(nums)
        nums = sorted(list(nums))
        res = 0
        ans = 1
        l = 0
        r = 1
        start = 0
        
        while r <= len(nums) - 1:
            if nums[r] == nums[l] + 1:
                res = r - start + 1
            else:
                start = r
            l = r
            r += 1
            
            ans = max(res, ans)
            
        return ans
                
