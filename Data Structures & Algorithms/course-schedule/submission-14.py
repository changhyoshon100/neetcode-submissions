class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle = set()
        visit = set()
        mp = defaultdict(list)

        for crs, pre in prerequisites:
            mp[crs].append(pre)

        def dfs(curr):
            if curr in cycle:
                return False
            # if curr in visit:
            #     return True
            
            cycle.add(curr)
            for nei in mp[curr]:
                if not dfs(nei):
                    return False
            cycle.remove(curr) 
            # visit.add(curr)

            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True