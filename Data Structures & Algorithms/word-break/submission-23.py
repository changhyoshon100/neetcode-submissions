class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = True
        words = set(wordDict)

        for i in range(len(s) - 1, -1, -1): # O(n) where n is length s
            for w in words:# O(m) m is length wordDict
                # O(k) k is length of word
                if i + len(w) <= len(s) and s[i:i + len(w)] in words and dp[i + len(w)]:
                    dp[i] = dp[i + len(w)]
        return dp[0] if dp[0] else False
        # time: O(mnk)
        # space: O(n + m*k)


