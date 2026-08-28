class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        visit = set()
        cycle = set()
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)

        def dfs(node, prev):
            if node in visit:
                return True

            visit.add(node)
            for nei in mp[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False

            return True
        
        cnt = 0
        for r in range(n):
            if r not in visit:
                if dfs(r,-1):                
                    cnt += 1
    
        return cnt
                