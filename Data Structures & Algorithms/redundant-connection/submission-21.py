class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        cycle = set()

        def dfs(crs, target):
            if crs in cycle:
                return True
            if crs == target:
                return False

            cycle.add(crs)
            for nei in mp[crs]:
                if not dfs(nei, target):
                    return False
            cycle.remove(crs)
            return True

        for a,b in edges:
            if a in mp and b in mp:
                if not dfs(a,b):
                    return [a,b]
                    
            mp[a].append(b)
            mp[b].append(a)
        
            