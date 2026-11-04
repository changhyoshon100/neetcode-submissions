class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        store = set()

        for n in nums:
            store.add(n)
        
        res = 0
        cnt = 0
        
        for n in nums:
            if n - 1 not in store:
                cnt = 0
                while n in store:
                    cnt += 1
                    n += 1
                res = max(res, cnt)
        return res if res != 0 else 1
                
