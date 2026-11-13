class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        visit = set()

        def dfs(crs,target):
            if crs == target:
                return False
                
            if crs in visit:
                return True
            visit.add(crs)

            for nei in mp[crs]:
                if not dfs(nei, target):
                    return False
            visit.remove(crs)
            return True

        for a,b in edges:
            if a in mp and b in mp:
                if not dfs(a,b):
                    return [a,b]
            mp[a].append(b)
            mp[b].append(a)
        