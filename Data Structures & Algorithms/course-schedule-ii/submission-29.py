class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)

        for a,b in prerequisites:
            mp[a].append(b)
        
        res = []
        visit = set()
        cycle = set()

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
            if i not in visit:
                if not dfs(i):
                    return []
        return res


        
        
