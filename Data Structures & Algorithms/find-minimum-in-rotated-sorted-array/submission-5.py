class Solution:
    def findMin(self, nums: List[int]) -> int:
        L,R = 0, len(nums) - 1
        res = float('infinity')
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                res = min(res, nums[mid])
                R = mid - 1
        return res


            