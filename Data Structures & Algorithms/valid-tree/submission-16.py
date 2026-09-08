class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for crs, pre in edges:
            mp[crs].append(pre)
            mp[pre].append(crs)
        
        cycle = set()
        visited = set()


        def dfs(crs, prev):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            
            cycle.add(crs)

            for nei in mp[crs]:
                if nei == prev:
                    continue
                if not dfs(nei, crs):
                    return False
            visited.add(crs)
            cycle.remove(crs)
            
            return True


        ans = dfs(0,-1)
        
        if len(visited) != n:
            return False
        return ans

