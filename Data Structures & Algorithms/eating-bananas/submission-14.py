class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1: return math.ceil(piles[0] / h)
        small, large = 1, max(piles)
        res = float('infinity')
        
        while small <= large:
            k = (small + large) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                large = k - 1
            else:
                small = k + 1
        return res 
            
            

        