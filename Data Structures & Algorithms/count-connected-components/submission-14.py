class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)

        visit = set()
        def dfs(curr, parent):
            if curr in visit:
                return True
            
            visit.add(curr)
            for nei in mp[curr]:
                if parent == nei:
                    continue
                if not dfs(nei, curr):
                    return 0
            return True
        cnt = 0
        
        for r in range(n):
            if r not in visit:
                if dfs(r,-1):
                    cnt += 1
            
        return cnt
        
            