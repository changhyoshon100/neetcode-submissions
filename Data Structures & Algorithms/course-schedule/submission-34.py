class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)

        for a,b in prerequisites:
            mp[a].append(b)
        cycle = set()
        visit = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            visit.add(crs)
            cycle.add(crs)
            for nei in mp[crs]: 
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            

            return True
        
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i):
                    return False
        return True

