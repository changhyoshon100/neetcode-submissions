class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        visited = set()
        cycle = set()
        res = []
        for crs, pre in prerequisites:
            mp[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for nei in mp[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        