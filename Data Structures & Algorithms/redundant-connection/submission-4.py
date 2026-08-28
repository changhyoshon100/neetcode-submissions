class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = {i:[] for i in range(1,len(edges)+1)}
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for nei in mp[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            visit.remove(i)
            
            return True
        
        for i,v in edges:
            mp[i].append(v)
            mp[v].append(i)
            
            if not dfs(i,0):
                return [i,v]
        