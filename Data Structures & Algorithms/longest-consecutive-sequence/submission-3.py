class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        st_nums = list(sorted(set(nums)))
        res = 1
        temp = 1
        print(st_nums)
        for i in range(len(st_nums)-1):
            if st_nums[i] + 1 == st_nums[i+1]:
                
                temp += 1
                res = max(res, temp)
            else:
                temp = 1
        return res
        