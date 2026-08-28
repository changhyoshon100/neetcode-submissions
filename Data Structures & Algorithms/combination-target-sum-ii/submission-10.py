class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        bucket = []
        candidates = sorted(candidates)
        memo = {}
        def dfs(cand, total, i):
            if total == target:
                if res not in bucket:
                    bucket.append(res.copy())
                    
                return bucket
            if total > target or i >= len(cand):
                return 0
            if tuple(res) in memo:
                return memo[tuple(res)]
            
            res.append(cand[i])
            dfs(cand, total + cand[i], i+1)
            val = res.pop()
            total -= val
            dfs(cand, total + cand[i], i+1)
            memo[tuple(res)] = bucket
            return bucket
        return dfs(candidates, 0, 0)