class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = 0
        while L <= R:
            hours = 0
            mid = (L + R) // 2
            for p in piles:
                hours += math.ceil(p / mid)
            if hours <= h:
                res = mid
                R = mid - 1
            else:
                L = mid + 1
        return res