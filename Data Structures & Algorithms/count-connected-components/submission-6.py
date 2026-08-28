class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = {i:[] for i in range(n)}
        for i,v in edges:
            adj[i].append(v)
            adj[v].append(i)
        res = 0
        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)
            for pre in adj[curr]:
                if pre == prev:
                    continue
                dfs(pre, curr)
            
            return True
        
        for i in range(n):
            if i in visit:
                continue
            if dfs(i,-1):
                res += 1
        return res
