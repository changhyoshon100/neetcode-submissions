class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        mp = defaultdict(list)
        
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

        for crs, pre in edges:
            mp[crs].append(pre)
            mp[pre].append(crs)

            if not dfs(crs, pre):
                return [crs, pre]
                
            
        