class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        cycle = set()
        
        mp = defaultdict(list)
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in mp[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res