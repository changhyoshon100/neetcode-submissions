class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        time = 0
        while low <= high:
            mid = (low + high) // 2
            for p in piles:
                time += math.ceil(p / mid)
            if time > h:
                low = mid + 1
            else:
                high = mid - 1
                res = mid
            time = 0
        return res
            
                

