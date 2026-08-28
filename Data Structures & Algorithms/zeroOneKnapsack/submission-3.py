class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # declare len of profit and cap
        N = len(profit)
        M = capacity
        # make [0] for dp with the size of M
        # it indicates the above row
        dp = [0] * (M + 1)
        
        # assign value of profit[0]
        for c in range(M + 1):
            if c >= weight[0]:
                dp[c] = profit[0]
        print(dp)

        # loop to decide include or not 
        # row is for profit, col is for cap
        for i in range(1, N):
            # declare current row
            curRow = [0] * (M + 1)
            print(curRow)
            for c in range(M + 1):
                # dp with column c
                skip = dp[c]
                # include to compare current and prev
                include = 0
                if c - weight[i] >= 0:
                    # compare prev row in col c and cur row + profit
                    include = profit[i] + dp[c - weight[i]]
                curRow[c] = max(include, skip)
            dp = curRow
        return dp[M]
