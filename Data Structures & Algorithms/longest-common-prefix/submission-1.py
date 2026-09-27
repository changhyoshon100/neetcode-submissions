class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(word) for word in strs])

        strs.sort()
        for i in range(min_len):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]

        return strs[0]
