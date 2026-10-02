class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        cycle = set()
        visit = set()
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for nei in mp[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)    
            visit.add(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
