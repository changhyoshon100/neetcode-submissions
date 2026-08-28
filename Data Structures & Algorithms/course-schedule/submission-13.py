class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle = set()
        visit = set()
        mp = defaultdict(list)
        for cur, pre in prerequisites:
            mp[cur].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in mp[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
