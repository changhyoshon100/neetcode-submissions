class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        
        visit = set()
        def dfs(crs,prev):
            if crs in visit:
                return True
            
            visit.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                dfs(nei,crs)

            return True
            
        res = 0
        for i in range(n):
            if i not in visit:
                if dfs(i,-1):
                    res += 1
        return res