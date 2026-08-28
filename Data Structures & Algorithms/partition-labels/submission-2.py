class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        count = defaultdict(int)
        for i,c in enumerate(s):
            count[c] = i
        farthest = 0
        size = 0
        for i,c in enumerate(s):
            farthest = max(farthest, count[c])
            size += 1
            if i >= farthest:
                res.append(size)
                size = 0
        return res


            