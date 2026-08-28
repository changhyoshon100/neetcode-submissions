class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        for s, e in edges:
            mp[s].append(e)
            mp[e].append(s)
        
        visit = set()


        def dfs(curr, prev):
            if curr in visit:
                return True

            visit.add(curr)
            for nei in mp[curr]:
                if prev == nei:
                    continue
                dfs(nei, curr)

            return True
        res = 0
        for c in range(n):
            if c not in visit:
                dfs(c,-1)
                res += 1
        return res
