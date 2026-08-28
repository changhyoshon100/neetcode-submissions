class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for i in range(len(prerequisites)):
            prereq, crs = prerequisites[i][0], prerequisites[i][1]
            adj[crs].append(prereq)
        
        mapVisit = {}
        def dfs(crs):
            if crs not in mapVisit:
                mapVisit[crs] = set()

                for prereq in adj[crs]:
                    mapVisit[crs] |= dfs(prereq)

                mapVisit[crs].add(crs)
            return mapVisit[crs]

        for i in range(numCourses):
            dfs(i)
        res = []
        for pre, crs in queries:
            res.append(pre in mapVisit[crs])
        return res
        