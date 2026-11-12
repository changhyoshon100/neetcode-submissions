class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        
        def dfs(crs, target, visit):
            if crs == target:
                return False
            
            visit.add(crs)

            for nei in mp[crs]:
                if nei not in visit:
                    if not dfs(nei, target, visit):
                        return False
            return True


        for a,b in edges:
            if a in mp and b in mp:
                if a not in visit:
                    if not dfs(a,b,visit):
                        return [a, b]
            visit = set()
            mp[a].append(b)
            mp[b].append(a)

        
