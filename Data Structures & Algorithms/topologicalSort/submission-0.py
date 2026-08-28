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
            if curr in visit:
                return True
            if curr in visiting:
                return False
            
            visiting.add(curr)
            for nei in adj[curr]:
                if not dfs(nei):
                    return False
            visiting.remove(curr)

            topSort.append(curr)
            visit.add(curr)

            return topSort

        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort

