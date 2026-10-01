class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # using heap because k closest
        # how to save in the heap (distance, x, y) using min heap

        heap = []
        for point in points:
            heapq.heappush(heap, [point[0] ** 2 + point[1] ** 2, point[0], point[1]])

        answer = []
        while k > 0:
            answer.append(heapq.heappop(heap)[1:])
            k -= 1

        return answer
        