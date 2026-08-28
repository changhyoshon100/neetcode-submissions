class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)

        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        
        cycle = set()
        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return False
            if curr in cycle:
                return False
            visit.add(curr)

            cycle.add(curr)
            for nei in mp[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            cycle.remove(curr)

            return True


        if dfs(0,-1) and len(visit) == n:
            return True
        else:
            return False
