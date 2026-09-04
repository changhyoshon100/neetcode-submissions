class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(i,j,par):
            if len(i) > n or len(j) > n:
                return 
            if len(i) < len(j):
                return
            if n == len(i) and n == len(j) and len(i) == len(j):
                res.append(par)
                return
            
            dfs(i + "(", j, par + "(")
            dfs(i, j + ")", par + ")")

        dfs("","","")
        return res