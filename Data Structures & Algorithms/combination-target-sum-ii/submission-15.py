class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []
        candidates.sort()
        def dfs(i, total):
            if total > target:
                return
            if i == len(candidates) and total != target:
                return
            if total == target:
                res.append(subsets.copy())
                return

            subsets.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subsets.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, total)
        
        dfs(0, 0)
        return res