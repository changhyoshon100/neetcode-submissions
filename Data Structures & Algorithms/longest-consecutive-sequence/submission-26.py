class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        dup = set()
        nums.sort()
        for n in nums:
            if n in dup:
                continue
            dup.add(n)
            if n - 1 not in nums:
                cnt = 1
                while n + cnt in nums:
                    cnt += 1
                res = max(cnt, res)
        return res