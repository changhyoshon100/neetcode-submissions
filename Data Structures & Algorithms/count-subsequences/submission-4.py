class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        # res = 0
        def dfs(i,j):
            # nonlocal res
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == t[j]:
                # move both
                a = dfs(i+1,j+1)
                # move i
                b = dfs(i+1,j)
                res = a + b
            else:
                res = dfs(i+1,j)
            memo[(i,j)] = res
            return res

                
        # ans = 0
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         ans = max(ans, dfs(i,j))
        # return ans
        return dfs(0,0)