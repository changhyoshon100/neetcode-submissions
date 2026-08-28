class Solution:
    def canPartition(self, nums: List[int]) -> bool:
# dfs sometimes returns None (because you return with no value). 
# Then the result becomes None instead of True/False.

# You don’t stop when i goes out of bounds.

# You call dfs(add + nums[i], ...) twice, and the second time you increment i 
# manually in a confusing way.

# return dfs(0,0) if True else False always returns dfs(0,0) (the if True is meaningless).

# Also you must check sum(nums) is even; otherwise it’s impossible.
        memo = set()
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)
        def dfs(curr, i):
            if i >= len(nums):
                return False
            if curr > target // 2:
                return False
            if curr == target // 2:
                return True
            if (i, curr) in memo:
                return False
            
            if dfs(curr, i+1):
                return True
            if dfs(curr + nums[i], i+1):
                return True
            
            memo.add((i, curr))
            return False
        
        return dfs(0, 0)
