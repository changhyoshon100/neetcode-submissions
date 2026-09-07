class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(i,j, chars):
            if i < j:
                return
            if i == n and j == n and i == j:
                res.append(chars)
                return
            if i == n+1 or j == n+1:
                return

            dfs(i+1,j, chars + '(')
            dfs(i,j+1, chars + ')')
        
        dfs(0,0, "")
        return res