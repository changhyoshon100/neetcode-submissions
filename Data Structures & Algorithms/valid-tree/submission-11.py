class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)
        # undirected
        for s, e in edges:
            mp[s].append(e)
            mp[e].append(s)
        cycle = set()
        visit = set()
    
        def dfs(curr, prev):
            if curr in cycle:
                return False
            if curr in visit:
                return True

            cycle.add(curr)
            for nei in mp[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            cycle.remove(curr)
            visit.add(curr)
            return True
                

        return dfs(0,-1) and len(visit) == n