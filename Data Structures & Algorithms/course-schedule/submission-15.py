class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        cycle = set()
        visited = set()

        for crs, pre in prerequisites:
            mp[crs].append(pre)

        def dfs(curr):
            if curr in visited:
                return True
            if curr in cycle:
                return False
            
            if mp[curr] == []:
                visited.add(curr)
                return True
            
            
            cycle.add(curr)
            for nei in mp[curr]:
                if not dfs(nei):
                    return False
            cycle.remove(curr)

            visited.add(curr)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True