class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr, comb = [], []
        
        def dfs(i, k, curr, comb):
            if len(curr) == k:
                comb.append(curr.copy())
                return 
            
            
            for j in range(i, n+1):
                curr.append(j)
                dfs(j+1, k, curr, comb)
                curr.pop()

        dfs(1, k, curr, comb)
        return comb