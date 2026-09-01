class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        store = set()
        for n in nums:
            store.add(n)
        
        cnt = 0
        res = 0

        for n in nums:
            if n - 1 not in store:
                cnt = 0
                while n in store:
                    cnt += 1
                    n += 1
                res = max(cnt, res)
        return res if res != 0 else 1

