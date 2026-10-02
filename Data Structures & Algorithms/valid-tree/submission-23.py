class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)

        for crs, pre in edges:
            mp[crs].append(pre)
            mp[pre].append(crs)
        
        cycle = set()
        visit = set()

        def dfs(crs,prev):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                if not dfs(nei,crs):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            return True
        
        if not dfs(0,-1):
            return False
        return True if len(visit) == n else False