class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        
        cycle = set()
        visit = set()
        res = []
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for nei in mp[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)

            visit.add(crs)
            res.append(crs)
            return True
        
        for r in range(numCourses):
            if not dfs(r):
                return []
            
        return res