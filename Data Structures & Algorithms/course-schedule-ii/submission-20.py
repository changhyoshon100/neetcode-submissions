class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        cycle = set()
        visit = set()

        mp = defaultdict(list)

        for a,b in prerequisites:
            mp[a].append(b)

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
            res.append(crs)
            return True

        for r in range(numCourses):
            if not dfs(r):
                return []

        return res