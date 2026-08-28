class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        visit = set()
        cycle = set()
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)

        def dfs(node):
            visit.add(node)
            for nei in mp[node]:
                if nei not in visit:
                    dfs(nei)

        
        cnt = 0
        for r in range(n):
            if r not in visit:
                dfs(r)
                cnt += 1
    
        return cnt
                