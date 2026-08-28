class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        ans = []
        c.sort()
        def dfs(i, total, res):
            nonlocal ans
            if total == target:
                ans.append(res.copy())
                return
            if i == len(c) or total > target:
                return

            total += c[i]
            res.append(c[i])
            dfs(i+1, total, res)
            res.pop()
            total -= c[i]


            j = i
            while j + 1 < len(c) and c[j] == c[j+1]:
                j += 1
            
            dfs(j+1, total, res)
            return ans
        return dfs(0,0,[])