class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subsets = []
        
        def dfs(i,j):
            if i < j:
                return 
            if i > n or j > n:
                return
            if i == n and j == n:
                temp = "".join(subsets)
                res.append(temp)
                return
            
            subsets.append('(')
            dfs(i+1,j)
            subsets.pop()
            subsets.append(')')
            dfs(i,j+1)
            subsets.pop()

        dfs(0,0)
        return res