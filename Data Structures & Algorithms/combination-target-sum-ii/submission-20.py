class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        cand.sort()
        res = []
        def dfs(i, total, subsets):
            if total == target:
                cp = subsets.copy()
                res.append(cp)
                return
            
            if i == len(cand):
                return
            
            if total > target:
                return

            subsets.append(cand[i])
            dfs(i+1, total + cand[i], subsets)
            subsets.pop()
            while i+1 < len(cand) and cand[i] == cand[i+1]:
                i += 1
            dfs(i+1, total, subsets)
            
        dfs(0, 0, [])
        return res