class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in check:
                cnt = 1
                while n + cnt in check:
                    cnt += 1
                res = max(res, cnt)
        return res