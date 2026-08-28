class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = []
        print(nums, target)
        for i,v in enumerate(nums):
            arr.append([v,i])

        arr.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            # print(i,j,arr)
            if arr[i][0] + arr[j][0] == target:
                return [min(arr[i][1],arr[j][1]),max(arr[i][1],arr[j][1])]
            elif arr[i][0] + arr[j][0] > target:
                j-=1
            elif arr[i][0] + arr[j][0] < target:
                i+=1
        return []


        
