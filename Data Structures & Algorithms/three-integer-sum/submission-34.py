class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    res.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
                
        return list(res)
            
