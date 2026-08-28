class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.dfs(0, 0, nums, target, [], [])
    def dfs(self, added, i, nums, target, res, subsets):
        if added == target:
            print('@@@', subsets, added, target)
            res.append(subsets.copy())
            return 

        if i >= len(nums) or added > target:
            return
        # if added > target:
        #     print("!!!!#####",subsets,added, target)
        #     # added -= nums[i]
        #     # subsets.pop()
        #     # i += 1
        #     return 
        

        
        subsets.append(nums[i])
        self.dfs(added + nums[i], i, nums, target, res, subsets)
        subsets.pop()
        
        
        self.dfs(added, i+1, nums, target, res, subsets)
        return res
