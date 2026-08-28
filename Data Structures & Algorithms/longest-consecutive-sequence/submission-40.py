class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()
        for n in nums:
            store.add(n)
        
        cnt = 0
        res = 0
        mp = defaultdict(int)
        for n in nums:
            if n in mp:
                continue
            if n - 1 in store:
                cnt = 1
            else:
                cnt = 0
            
            while n in store:
                cnt += 1
                n += 1
                res = max(res, cnt)
                mp[n] = res
        return res
                



