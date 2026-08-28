class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums)*2)
        ans[:len(nums)] = nums
        ans[len(nums):] = nums
        return ans