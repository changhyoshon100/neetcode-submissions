class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        visit = set()
        def dfs(curr):
            if curr in visit:
                return None
            visit.add(curr)
            for nei in mp[curr]:
                dfs(nei)
                
        cnt = 0
        for r in range(n):
            if r not in visit:
                dfs(r)
                cnt += 1
        return cnt
