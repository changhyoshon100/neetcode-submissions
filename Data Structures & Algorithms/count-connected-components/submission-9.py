class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        for s, e in edges:
            mp[s].append(e)
            mp[e].append(s)
        
        visit = set()
        cycle = set()

        def dfs(curr, prev):
            if curr in cycle:
                return True
            if curr in visit:
                return True

            cycle.add(curr)
            for nei in mp[curr]:
                if prev == nei:
                    continue
                dfs(nei, curr)
                    
            cycle.remove(curr)
            visit.add(curr)
            return True
        res = 0
        for c in range(n):
            if c not in visit:
                dfs(c,-1)
                res += 1
        return res
