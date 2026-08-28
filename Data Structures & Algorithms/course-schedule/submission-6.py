class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for i in range(len(prerequisites)):
            u,v = prerequisites[i][0], prerequisites[i][1]
            adj[u].append(v)

        visit = set()
        visiting = set()
        topSort = [] 
        def dfs(curr):
            if curr in visiting:
                return False
            # if adj[curr] == []:
            #     return True
            if curr in visit:
                return True
            
            
            visiting.add(curr)
            for nei in adj[curr]:
                if not dfs(nei):
                    return False
            visiting.remove(curr)
            
            visit.add(curr)
            # adj[curr] = []
            return True
        
        for i in range(len(prerequisites)):
            if not dfs(i):
                return False
        return True
