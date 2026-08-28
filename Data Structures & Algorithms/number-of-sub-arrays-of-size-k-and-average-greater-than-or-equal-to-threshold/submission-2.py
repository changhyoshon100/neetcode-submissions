class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        cnt = 0
        total = 0
        for i in range(L, L + k):
            total += arr[i]
        
        if total / k >= threshold:
            cnt += 1

        for R in range(k, len(arr)):    
            total += arr[R]
            total -= arr[L]
            if R - L == k and (total / k)  >= threshold:
                cnt += 1
            L += 1
            
        return cnt
            


