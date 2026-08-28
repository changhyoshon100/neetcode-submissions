class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = defaultdict(int)
        res = 0
        L = 0
        for R in range(len(s)):
            check[s[R]] += 1
            while (R - L + 1) - max(check.values()) > k:
                check[s[L]] -= 1
                L += 1
                print(R, L )
            res = max(res, R - L + 1)
        return res 
            