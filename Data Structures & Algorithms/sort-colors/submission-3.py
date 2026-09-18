class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = [0] * 3

        for num in nums:
            bucket[num] += 1
        
        idx = 0
        for i in range(len(nums)):
            
            while bucket[idx] == 0:
                idx += 1
            
            nums[i] = idx
            bucket[idx] -= 1