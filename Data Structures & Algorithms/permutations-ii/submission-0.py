class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        ans = set()
        
        for n in nums:
            nextPerms = []
            for p in perms:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    nextPerms.append(pCopy)
                    if len(pCopy) == len(nums):
                        ans.add(tuple(pCopy))
            perms = nextPerms    
        return list(ans)