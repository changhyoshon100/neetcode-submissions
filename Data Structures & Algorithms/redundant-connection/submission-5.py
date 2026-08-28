class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(1,len(edges)+1)}
        visit = set()
        
        
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            visit.remove(i)
            return True
            
        for i,v in edges:
            adj[i].append(v)
            adj[v].append(i)

            if not dfs(i,0):
                return [i,v]
    