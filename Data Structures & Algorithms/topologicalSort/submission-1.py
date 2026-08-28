class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            u,v = edges[i][0], edges[i][1]
            adj[u].append(v)
        
        visit = set()
        visiting = set()
        topSort = []

        def dfs(curr):
            if curr in visiting:
                return False
            if curr in visit:
                return True
            
            visiting.add(curr)
            for nei in adj[curr]:
                if not dfs(nei):
                    return False
            visiting.remove(curr)

            visit.add(curr)
            topSort.append(curr)
            return topSort

        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort


        