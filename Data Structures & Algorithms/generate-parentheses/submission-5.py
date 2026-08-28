class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        bucket = []
        def dfs(openN, closeN):
            if openN == closeN == n:
                print(res)
                bucket.append(''.join(res))
                return bucket

            if openN < n:
                res.append('(')
                dfs(openN + 1, closeN)
                res.pop()

            if closeN < openN:
                res.append(')')
                dfs(openN, closeN + 1)
                res.pop()
            return bucket
        return dfs(0,0)