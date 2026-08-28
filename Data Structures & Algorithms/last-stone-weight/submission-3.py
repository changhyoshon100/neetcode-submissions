class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        i = len(stones) - 1
        while i >= 1:
            stones = sorted(stones)
            # print(stones)
            stones[i-1] = abs(stones[i] - stones[i-1])
            stones.pop()
            i -= 1
        return stones[0]
    
        