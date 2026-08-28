class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visit = set()

        for i,v in edges:
            adj[i].append(v)
            adj[v].append(i)
        print(adj)
        
        def dfs(i, prev):
            print('i:',i)
            if i in visit:
                return 0
            
            visit.add(i)
            
            for j in adj[i]:
                if j == prev:
                    continue
                
                dfs(j, i)
                    
            return 1
        res = 0
        for i in range(n):
            res += dfs(i,i-1)
        return res