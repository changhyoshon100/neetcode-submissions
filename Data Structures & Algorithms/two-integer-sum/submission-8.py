class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,v in enumerate(nums):
            diff = target - nums[i]
            if diff in prevMap:
                return [min(i, prevMap[diff]), max(i, prevMap[diff])]
            prevMap[v] = i
        return []