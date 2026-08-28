class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1

        ans = 0

        def cmp(x):
            return (x < 0) - (x > 0)

        def dfs(i, prev, cur):
            nonlocal ans
            if i == len(arr) - 1:
                ans = max(ans, cur)
                return ans
            
            c = cmp(arr[i+1] - arr[i])

            if c == 0:
                cur = 1
                prev = 0
            elif prev == 0 or c * prev < 0:
                cur += 1
                prev = c
            else:
                cur = 2
                prev = c
            ans = max(ans, cur)
            dfs(i+1, prev, cur)

            return ans
        return dfs(0,0,1)
