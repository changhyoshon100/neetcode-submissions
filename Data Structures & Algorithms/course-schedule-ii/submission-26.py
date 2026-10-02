class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        cycle = set()
        res = []
        mp = defaultdict(list)
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
            res.append(crs)
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res