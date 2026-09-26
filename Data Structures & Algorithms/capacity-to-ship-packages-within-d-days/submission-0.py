class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = left + (right - left) // 2
            d = 1
            max_weight = mid
            for w in weights:
                if max_weight >= w:
                    max_weight -= w
                else:
                    d += 1
                    max_weight = mid -w
            
            if d > days:
                left = mid + 1
            else:
                right = mid - 1
            
        return left