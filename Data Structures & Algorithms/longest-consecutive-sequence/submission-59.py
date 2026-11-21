class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        store = set()

        for n in nums:
            store.add(n)
        res = 1
        for n in nums:
            if n - 1 not in store:
                cnt = 0
                while n in store:
                    n += 1
                    cnt += 1
                res = max(res, cnt)
        return res
                

