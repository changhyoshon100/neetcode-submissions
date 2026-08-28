class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        bucket = []
        res = []
        memo = {}
        candidates = sorted(candidates)
        def dfs(cand, i, total):
            if total == target:
                if res not in bucket:
                    bucket.append(res.copy())

                return bucket
            if total > target or i >= len(cand):
                return 0
            if tuple(res) in memo:
                return memo[tuple(res)]
            

            res.append(cand[i])
            total = total + cand[i]
            
            dfs(cand, i+1, total)
            val = res.pop()
            total -= val
            # print(res, total)
            dfs(cand, i+1, total)
            
            memo[tuple(res)] = target
            return bucket
        return dfs(candidates, 0, 0)