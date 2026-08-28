class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        candidates.sort()
        def dfs(can, i, val):
            if val == target:
                res.append(arr.copy())
                return
            if val > target or i == len(can):
                return 
            
            arr.append(can[i])
            dfs(can, i+1, val + can[i])
            arr.pop()

            while i+1 < len(can) and can[i] == can[i+1]:
                i += 1
            dfs(can, i+1, val)
        
        dfs(candidates, 0, 0)
        return res