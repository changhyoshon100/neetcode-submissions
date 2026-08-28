class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        bucket = set()
        def dfs(i, res):
            if i == len(res):
                bucket.add(tuple(ans.copy()))
                return bucket
            
            ans.append(res[i])
            dfs(i+1, res)
            ans.pop()
            dfs(i+1, res)
            return bucket
        
        return list(dfs(0, nums))
        