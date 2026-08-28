class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        print(mp)
        res = []
        for i in list(mp.keys()):
            if mp[i] in sorted(list(mp.values()))[-k:]:
                res.append(i)
        return res