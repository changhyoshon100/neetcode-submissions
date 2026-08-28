class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(i, total, res):
            nonlocal ans 
            if total == target:
                ans.append(res.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            total += candidates[i]
            res.append(candidates[i])
            dfs(i+1, total, res)

            res.pop()
            total -= candidates[i]
            j = i
            while j + 1 < len(candidates) and candidates[j] == candidates[j+1]:
                j += 1
            
            dfs(j+1, total, res)

            return ans
        
        return dfs(0,0,[])