class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    cp = p.copy()
                    cp.insert(i, n)
                    newPerms.append(cp)
            perms = newPerms
        return perms