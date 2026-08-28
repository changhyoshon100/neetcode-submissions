class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums)
        k = k % r
        
        def dfs(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            return nums

        dfs(0,r-1)
        dfs(0,k-1)
        dfs(k,r-1)
            
        return nums
