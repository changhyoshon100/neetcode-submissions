class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(i, j, subsets): 
            if i == n and j == n:
                cp = subsets.copy()
                st = ''.join(subsets)
                res.append(st)
                return

            if i >= n + 1 or j >= n + 1:
                return
            if i >= j:
                subsets.append('(')
                dfs(i+1, j, subsets)
                subsets.pop()
                
                subsets.append(')')
                dfs(i, j+1, subsets)
                subsets.pop()
            
        dfs(0, 0, [])
        return res