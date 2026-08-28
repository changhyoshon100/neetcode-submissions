class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for i in range(len(prerequisites)):
            u,v = prerequisites[i][0], prerequisites[i][1]
            adj[u].append(v)

        visit = set()
        visiting = set()
        topSort = []
        def dfs(curr):
            # check loop
            if curr in visiting:
                return False
            # check end node
            if curr in visit:
                return True
            
            visiting.add(curr)
            for nei in adj[curr]:
                if not dfs(nei):
                    return False
            visiting.remove(curr)
            visit.add(curr)
            topSort.append(curr)
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return topSort


        