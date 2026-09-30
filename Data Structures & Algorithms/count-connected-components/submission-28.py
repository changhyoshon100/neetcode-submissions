class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        cycle = set()

        mp = defaultdict(list)
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        
        def dfs(crs,prev):
            # if crs in cycle:
            #     return False
            if crs in visit:
                return True
            
            # cycle.add(crs)
            visit.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                dfs(nei,crs)
            
            # cycle.remove(crs)
            
            return True
        res = 0
        for i in range(n):
            if i not in visit:
                if dfs(i,-1):
                    res += 1
        return res

