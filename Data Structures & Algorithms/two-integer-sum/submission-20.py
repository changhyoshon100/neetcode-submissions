class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}

        for i in range(len(nums)):
            if target - nums[i] in idxMap:
                return [idxMap[target - nums[i]], i]
            idxMap[nums[i]] = i
            
            

            
