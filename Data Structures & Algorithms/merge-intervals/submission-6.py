class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        for i in range(len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                output[-1][1] = max(intervals[i][1], output[-1][1])
            else:
                output.append(intervals[i])
        return output

