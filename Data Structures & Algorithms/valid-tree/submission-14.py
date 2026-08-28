class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        
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
        ans = dfs(0,-1)
        
        if not ans: return False
        return len(visit) == n 
        