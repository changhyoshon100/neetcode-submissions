class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid = no cycle, all nodes connects -> can do only one element
        adj = {i:[] for i in range(n)}
        visit = set()

        # undirected
        for i,v in edges:
            adj[i].append(v)
            adj[v].append(i)
        
        def dfs(crs,prev):
            if crs in visit:
                return False
            visit.add(crs)
            for pre in adj[crs]:
                if pre == prev:
                    continue
                if not dfs(pre, crs):
                    return False
            return True
            
        return dfs(0,-1) and len(visit) == n
        
        