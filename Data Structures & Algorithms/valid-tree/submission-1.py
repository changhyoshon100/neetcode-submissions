class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        visit = set()

        for i,v in edges:
            adj[i].append(v)
            adj[v].append(i)
        
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True 
        return dfs(0,-1) and len(visit) == n