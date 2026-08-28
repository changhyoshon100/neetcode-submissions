class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        res = []
        cycle = set()
        visit = set()
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visit:
                return True
            
            cycle.add(curr)
            for nei in mp[curr]:
                if not dfs(nei):
                    return False
            cycle.remove(curr)
            visit.add(curr)
            res.append(curr)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res  

