class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        for crs, pre in edges:
            mp[crs].append(pre)
            mp[pre].append(crs)
        
        visit = set()
        cycle = set()

        def dfs(crs, prev):
            if crs in visit:
                return True
                
            visit.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                dfs(nei, crs)
                
            
            return True
        res = 0
        for i in range(n):
            if i not in visit:
                if dfs(i,-1):
                    res += 1
        return res if len(visit) == n else -1

