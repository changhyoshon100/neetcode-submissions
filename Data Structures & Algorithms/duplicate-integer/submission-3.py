class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contain = set()
        for n in nums:
            if n in contain:
                return True
            contain.add(n)
        return False