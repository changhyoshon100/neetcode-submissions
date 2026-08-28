class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        def dfs(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        while L < R:
            if s[L] != s[R]:
                return (dfs(L+1, R) or dfs(L, R-1))
            
            L += 1
            R -= 1
        return True