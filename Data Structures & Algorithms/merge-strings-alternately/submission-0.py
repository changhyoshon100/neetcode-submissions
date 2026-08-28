class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        minLen = min(len(word1), len(word2))
        for i in range(minLen):
            res += word1[i]
            res += word2[i]
        newWord = ""
        maxLen = max(len(word1), len(word2))
        if maxLen == len(word1):
            newWord = word1
        else:
            newWord = word2
            
        for i in range(minLen, maxLen):
            res += newWord[i]
        return res