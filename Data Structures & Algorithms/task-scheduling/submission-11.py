import heapq
from collections import defaultdict
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num = len(tasks)
        freq_dict = defaultdict(int)

        for task in tasks:
            freq_dict[task] += 1

        heap = []
        for task, freq in freq_dict.items():
            heapq.heappush(heap, [-freq, task])

        min_num = 0

        while num > 0:
            task_set = {char for _, char in heap}
            pending = []
            used = 0

            while task_set and used < n + 1:
                freq, char = heapq.heappop(heap)
                task_set.remove(char)

                freq += 1
                num -= 1
                used += 1
                min_num += 1

                if freq < 0:
                    pending.append([freq, char])

            if num > 0:
                min_num += n + 1 - used

            for item in pending:
                heapq.heappush(heap, item)

        return min_num