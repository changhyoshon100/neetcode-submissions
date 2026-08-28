class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.arr = []
        total = 0
        for i in range(len(self.nums)):
            total += self.nums[i]
            self.nums[i] = total
        

    def sumRange(self, left: int, right: int) -> int:

        return self.nums[right] - self.nums[left-1] if left > 0 else self.nums[right]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)