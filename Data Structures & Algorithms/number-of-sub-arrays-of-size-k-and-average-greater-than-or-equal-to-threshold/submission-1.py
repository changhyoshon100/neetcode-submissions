class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        def filter(val,k):
            if val/k >= threshold:
                return True
            return False

        res = 0
        N = len(arr)
        L = 0
        cnt = 0
        for R in range(N):
            res += arr[R]
            if R - L + 1 > k:
                res -= arr[L]
                L += 1
            if R - L + 1 == k:
                if filter(res, k):
                    cnt += 1
            
        return cnt
            