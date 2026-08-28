class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for s,e in edges:
            mp[s].append(e)
            mp[e].append(s)

        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return False
            visit.add(curr)
            for nei in mp[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True

        return dfs(0,-1) and len(visit) == n
           