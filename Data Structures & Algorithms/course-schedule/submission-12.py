class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if mp[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in mp[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            mp[crs] = []
            return True
        res = True
        for c in range(numCourses):
            res = res and dfs(c)
        return res