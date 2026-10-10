class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = defaultdict(int)
        for i,v in enumerate(s):
            mp[v] = i
        
        farthest = 0
        res = []
        size = 0
        for i,v in enumerate(s):
            farthest = max(farthest, mp[v])
            size += 1
            if i >= farthest:
                res.append(size)
                size = 0
        return res
