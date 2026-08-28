class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        comparison = list(sorted(set(nums)))
        cnt = 0
        print(comparison)
        for i in range(len(comparison)):
            if nums[i] != comparison[i]:
                nums[i] = comparison[i]
            cnt = i
        nums = nums[:cnt+1]
        return len(nums)