class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, can, total):
            if total == target:
                res.append(can.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            can.append(candidates[i])
            dfs(i+1, can, total + candidates[i])
            can.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, can, total)
        dfs(0, [], 0)
        return res
