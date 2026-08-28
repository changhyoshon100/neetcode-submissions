class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        visiting = set()
        end = set()
        order = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in end:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            end.add(crs)
            order.append(crs)
            
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return []
            
        return order
