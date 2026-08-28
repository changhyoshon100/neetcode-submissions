class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = set()
        adj = {i:[] for i in range(1,len(edges)+1)}
        
        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            visit.remove(curr)
            return True
            
        

        for i,v in edges:
            adj[i].append(v)
            adj[v].append(i)
            
            if not dfs(i,v):
                return [i,v]

        
        
