class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = set()
        mp = defaultdict(list)

        res = []
        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)
            for nei in mp[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            visit.remove(curr)
            
            return True
        
        for s,e in edges:
            mp[s].append(e)
            mp[e].append(s)

            if not dfs(s,e):
                return [s,e]
        
        
