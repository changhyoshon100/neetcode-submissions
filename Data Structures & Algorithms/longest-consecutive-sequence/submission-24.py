class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        elif len(list(set(nums))) == 1: return 1
        check = set(nums)
        
        res = 1
        for n in nums:
            if n - 1 not in check:
                cnt = 1
                while n + cnt in check:
                    cnt += 1
                res = max(res, cnt)
                    
        return res
                