class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        mp = defaultdict(int)
        for n in hand:
            mp[n] += 1
        minH = list(mp.keys())
        heapq.heapify(minH)
        
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in mp:
                    return False
                mp[i] -= 1
                if mp[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True                    
