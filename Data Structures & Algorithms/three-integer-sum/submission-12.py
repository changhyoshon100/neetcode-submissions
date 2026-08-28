class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,v in enumerate(nums):
            L,R = i + 1, len(nums) - 1
            while L < R:
                if v + nums[L] + nums[R] < 0:
                    L += 1
                elif v + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    if [v, nums[L], nums[R]] not in res:
                        res.append([v, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return res
