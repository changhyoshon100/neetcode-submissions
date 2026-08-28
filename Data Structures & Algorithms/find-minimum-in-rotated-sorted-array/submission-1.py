class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = 0
        
        while nums[left] > nums[right]:
            mid = (left + right) // 2
            # print(nums[mid])
            if nums[mid] < nums[right]:
                left = mid + 1
                break
            else:
                left = mid + 1
        # print(left)
        while nums[left-1] < nums[left]:
            left -= 1
        return nums[left]
        

        