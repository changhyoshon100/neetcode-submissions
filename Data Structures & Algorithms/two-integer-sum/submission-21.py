class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict key: number value: idx
        num_idx = {}

        for i, num in enumerate(nums):
            if (target - num) in num_idx:
                return [num_idx[target - num], i]
            num_idx[num] = i

        return []