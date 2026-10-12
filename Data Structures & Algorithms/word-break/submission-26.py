class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        words = set(wordDict)

        for i in range(len(s) - 1, -1, -1):
            for word in words:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] = dp[i+len(word)]
        return dp[0]