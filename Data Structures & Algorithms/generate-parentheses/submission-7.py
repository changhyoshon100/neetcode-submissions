class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        bucket = []
        
        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(bucket))
                return
            
            if openN < n:
                bucket.append('(')
                dfs(openN + 1, closeN)
                bucket.pop()
            
            if closeN < openN:
                bucket.append(')')
                dfs(openN, closeN + 1)
                bucket.pop()
        
        dfs(0,0)
        return res