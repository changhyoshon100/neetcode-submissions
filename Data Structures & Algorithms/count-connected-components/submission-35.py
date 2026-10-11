class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        for crs, pre in edges:
            mp[crs].append(pre)
            mp[pre].append(crs)
        
        res = 0
        visited = set()
        cycle = set()

        def dfs(crs, prev):
            if crs in visited:
                return True

            visited.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                dfs(nei, crs)
                
        
            return True
        
        for i in range(n):
            if i not in visited:
                if dfs(i,-1):
                    res += 1
        return res if len(visited) == n else -1




