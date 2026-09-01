class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hours = 0
        a,b = 1, max(piles)
        ans = float('inf')
        while a <= b:
            mid = (a + b) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours > h:
                a = mid + 1
            else:
                ans = min(ans, mid)
                b = mid - 1
                
        return ans if ans != float('inf') else 0