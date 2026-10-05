class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # cheapest price -> dijkstra 
        # with condition n -> bellman ford
        mp = defaultdict(list)
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1): # O(k)
            tmpPrices = prices.copy() # time: O(n) where n is length of flights
            for s,d,p in flights: # O(n)
                mp[s].append((p,d))
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return prices[dst] if prices[dst] != float('inf') else -1
        # time: O(k*2n) -> O(kn)
        # space: O(n) 
            

            