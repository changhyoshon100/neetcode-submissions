class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * (len(nums))
        print(arr)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    # print(arr[i], arr[j])
                    arr[i] *= nums[j]
            
        return arr
            
            
