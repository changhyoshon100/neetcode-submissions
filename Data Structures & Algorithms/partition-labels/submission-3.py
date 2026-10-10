class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = defaultdict(int)
        farthest = 0
        size = 0
        res = []
        for i,v in enumerate(s):
            mp[v] = i

        for i,v in enumerate(s):
            farthest = max(farthest, mp[v])
            size += 1
            if farthest <= i:
                res.append(size)
                size = 0
        return res