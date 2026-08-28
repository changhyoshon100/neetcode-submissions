class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        K = 0
        visit = set()
        for R in range(len(nums)):

            if nums[R] in visit:
                continue
            visit.add(nums[R])
            nums[L] = nums[R]
            
            L += 1
            
        return len(nums[:L])

