class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for crs, pre in edges:
            mp[crs].append(pre)
            mp[pre].append(crs)

        visited = set()
        cycle = set()

        
        
        def dfs(curr, prev):
            if curr in cycle:
                return False
            if curr in visited:
                return True
            
            cycle.add(curr)
            for nei in mp[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            visited.add(curr)
            cycle.remove(curr)
            
            return True
            
        ans = dfs(0,-1)
        if len(visited) != n:
            return False
        return ans