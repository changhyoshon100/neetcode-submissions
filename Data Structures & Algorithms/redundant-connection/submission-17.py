class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        cycle = set()
        visit = set()

        def dfs(crs, prev):
            if crs in cycle:
                return False

            cycle.add(crs)
            for nei in mp[crs]:
                if nei == prev:
                    continue
                if not dfs(nei, crs):
                    return False
            cycle.remove(crs)
                
            return True

        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)

            if not dfs(a, b):
                return [a,b]

