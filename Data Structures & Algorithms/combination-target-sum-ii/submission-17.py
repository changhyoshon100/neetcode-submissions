class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, total, sub):
            nonlocal res
            if total > target:
                return
            if total == target:
                res.append(sub.copy())
                return 
            if i == len(candidates) and target != total:
                return 

            sub.append(candidates[i])
            dfs(i+1, total + candidates[i], sub)
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            sub.pop()
            dfs(i+1, total, sub)
            
        dfs(0, 0, [])
        return res