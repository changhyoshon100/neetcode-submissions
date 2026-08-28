class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        adj = {i:[] for i in range(n)}
        for i,v in edges:
            adj[i].append(v)
            adj[v].append(i)
        
        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        