class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)

        for crs, pre in edges:
            mp[crs].append(pre)
            mp[pre].append(crs)
        
        visited = set()
        cycle = set()
        def dfs(crs, prev):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                dfs(nei, crs)
            cycle.remove(crs)
            visited.add(crs)

            return True

        res = 0
        for i in range(n):
            if i not in visited:
                if dfs(i,-1):
                    res += 1
        
        return res