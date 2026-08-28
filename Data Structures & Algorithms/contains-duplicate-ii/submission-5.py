class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        dup = set()
        check = deque()

        for i in range(k):
            if nums[i] in dup:
                return True
            dup.add(nums[i])
            check.append(nums[i])
            
        
        while k <= len(nums)-1:
            if nums[k] in dup:
                return True
            check.append(nums[k])
            left = check.popleft()
            dup.add(nums[k])
            dup.remove(left)
            k += 1
        return False
            
            

        


