class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visit = set()
        N = len(nums)
        L = 0
        for R in range(N):
            if nums[R] in visit:
                return True
            visit.add(nums[R])
            if R - L + 1 > k:
                visit.remove(nums[L])
                L += 1
        return False
