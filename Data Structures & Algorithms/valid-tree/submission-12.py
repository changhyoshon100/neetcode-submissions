class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)

        for s,e in edges:
            mp[s].append(e)
            mp[e].append(s)
        
        cycle = set()

        def dfs(curr, prev):
            if curr in cycle:
                return False
            

            cycle.add(curr)
            print(curr)
            for nei in mp[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False

            return True
        
        ans = dfs(0,-1) 
        return ans if len(cycle) == n else False