class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0,1,2]
        s_bucket = [0,0,0]
        idx = 0
        for i in range(len(nums)):
            s_bucket[bucket[nums[i]]] += 1

        i = 0
        for s in s_bucket:
            while s > 0:
                nums[idx] = bucket[i]
                s -= 1
                idx += 1
            i+=1
        return nums

            