class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return right
        pivot = findMin(nums)
        left_arr = nums[:pivot]
        right_arr = nums[pivot:]

        def search(arr):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        a = search(left_arr)
        b = search(right_arr)
        # print(a,b, pivot)
        if a != -1:
            return a
        if b != -1:
            return b + len(left_arr)
        return -1
