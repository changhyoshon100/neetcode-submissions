class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = 0
        while left <= right:
            hours = 0
            mid = (left + right) // 2
            for p in piles:
                hours += math.ceil(p / mid)
            if hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res