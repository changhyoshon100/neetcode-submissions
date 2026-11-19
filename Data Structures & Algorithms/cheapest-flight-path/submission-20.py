class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        arr = [float('inf')] * (n + 1)
        arr[src] = 0
        for i in range(k+1):
            cp = arr.copy()
            for s,d,w in flights:
                if arr[s] + w < cp[d]:
                    cp[d] = arr[s] + w
            arr = cp
        return arr[dst] if arr[dst] != float('inf') else -1

                