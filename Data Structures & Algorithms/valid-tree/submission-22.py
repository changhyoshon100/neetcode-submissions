class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)

        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        
        cycle = set()
        visit = set()

        def dfs(crs,prev):
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                if not dfs(nei, crs):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            
            
            return True
            
        dfs(0,-1)
        return len(list(visit)) == n