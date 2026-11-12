class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)

        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        
        cycle = set()
        visit = set()
        
        def dfs(crs, prev):
            if crs in visit:
                return True
            if crs in cycle:
                return True
            
            cycle.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                if not dfs(nei, crs):
                    return False
            visit.add(crs)
            # cycle.remove(crs)
            

            return True    

                
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                res += 1
        return res


