class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        small, large = 1, max(piles)
        res = float('inf')
        while small <= large:
            mid = (small + large) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            if hours <= h:
                res = min(res, mid)
                large = mid - 1
            else:
                small = mid + 1
        return res
            


