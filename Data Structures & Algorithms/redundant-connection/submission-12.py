class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        visited = set()
        cycle = set()

        def dfs(crs, prev):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for nei in mp[crs]:
                if prev == nei:
                    continue
                if not dfs(nei, crs):
                    return False
            cycle.remove(crs)
            return True

        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)

            if not dfs(a,b):
                return [a,b]