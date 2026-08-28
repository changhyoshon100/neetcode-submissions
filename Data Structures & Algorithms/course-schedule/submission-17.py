class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        
        cycle = set()
        visited = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            if mp[crs] == []:
                return True
            
            cycle.add(crs)
            for nei in mp[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visited.add(crs)

            return True

        for r in range(numCourses):
            if not dfs(r):
                return False
        return True

