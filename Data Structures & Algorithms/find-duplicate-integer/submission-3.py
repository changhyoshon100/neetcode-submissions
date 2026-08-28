class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        rep = set()
        for n in nums:
            if n in rep:
                return n
            rep.add(n)
            
            