class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        cnt = 0
        subtotal = 0
        for i in range(k):
            subtotal += arr[i]
        
        if subtotal / k >= threshold: cnt = 1
        for i in range(k, len(arr)):
            subtotal = (subtotal + arr[i] - arr[i-k])
            if subtotal / k >= threshold:
                cnt += 1
            
        return cnt
            
