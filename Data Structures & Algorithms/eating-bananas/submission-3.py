class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        res = high
        time = 0
        while high >= low:
            mid = (high + low) // 2
            for p in piles:
                time += math.ceil(p / mid)
            
            if time <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
            time = 0
        return res
                
                
                

            
