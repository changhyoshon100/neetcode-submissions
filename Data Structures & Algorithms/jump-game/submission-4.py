class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if i in memo:
                return memo[i]
            # if nums[i] == 0:
            #     memo[(i)] = False
            #     return False
            
            for step in range(1, nums[i] + 1):
                # k = 1
                # while k <= n:
                #     dfs(i + k)
                #     k += 1
                if dfs(i + step):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        
        return dfs(0)
        # print(memo)
        
        