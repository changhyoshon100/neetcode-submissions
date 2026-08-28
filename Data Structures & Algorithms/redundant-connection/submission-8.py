class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        cycle = set()
        def dfs(curr, prev):
            if curr in cycle:
                return False
            
            cycle.add(curr)
            for nei in mp[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            cycle.remove(curr)

            return True
            
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
            if not dfs(a,b):
                return [a,b]

