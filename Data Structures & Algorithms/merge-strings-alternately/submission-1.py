class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        short_len = min(len(word1), len(word2))

        for i in range(short_len):
            res += word1[i]
            res += word2[i]

        res += word1[short_len:]
        res += word2[short_len:]

        return res