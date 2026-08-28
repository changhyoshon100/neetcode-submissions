class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visit = set()
        for n in nums:
            if n in visit:
                return n
            visit.add(n)