class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        ans = [0] * (len_nums * 2)

        for i in range(len_nums * 2):
            ans[i] = nums[i % len_nums]
        
        return ans
        