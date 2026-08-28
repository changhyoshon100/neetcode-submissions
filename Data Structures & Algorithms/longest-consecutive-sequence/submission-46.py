class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        store = set()

        for n in nums:
            store.add(n)

        res = 1
        for n in nums:
            if n - 1 not in store:
                cnt = 1
                while n in store:
                    cnt += 1
                    n += 1
                res = max(res, cnt)
        return res - 1







