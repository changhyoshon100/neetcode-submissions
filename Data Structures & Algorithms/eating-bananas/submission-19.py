class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        hours = 0
        res = float('inf')
        while L <= R:
            hours = 0
            mid = (L + R) // 2
            for p in piles:
                div = p // mid
                val = math.ceil(p / mid) - div
                hours += (div + val)
            
            if hours <= h:
                R = mid - 1
                res = min(res, mid)
            else:
                L = mid + 1
        return res
            



