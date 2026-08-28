class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for i in range(len(prerequisites)):
            prereq,crs = prerequisites[i][0], prerequisites[i][1]
            adj[crs].append(prereq)
        
        
        mapVisit = {}
        def dfs(crs):
            if crs not in mapVisit:
                mapVisit[crs] = set()
                
                for pre in adj[crs]:
                    mapVisit[crs] |= dfs(pre)
                mapVisit[crs].add(crs)
            return mapVisit[crs]
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u,v in queries:
            res.append(u in mapVisit[v])
        return res
                