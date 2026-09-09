class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
                result = max(result, temp)
            else:
                temp = 0

        return result

