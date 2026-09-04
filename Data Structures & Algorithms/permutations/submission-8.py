class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            newPerm = []
            for p in perms:
                for i in range(len(p) + 1):
                    cp = p.copy()
                    cp.insert(i, n)
                    newPerm.append(cp)
            perms = newPerm
        return perms