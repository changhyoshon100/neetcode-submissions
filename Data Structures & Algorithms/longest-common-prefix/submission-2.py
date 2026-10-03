class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        shortest_len = min([len(s) for s in strs])

        for i in range(shortest_len):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i] if i > 0 else ""

        return strs[0][:shortest_len]