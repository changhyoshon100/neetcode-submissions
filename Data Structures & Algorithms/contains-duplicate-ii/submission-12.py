class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        visit = set()
        L = 0
        for R in range(len(nums)):
            if nums[R] in visit:
                return True
            if R - L + 1 > k:
                visit.remove(nums[L])
                L += 1
            
            visit.add(nums[R])
        return False
        
            

            