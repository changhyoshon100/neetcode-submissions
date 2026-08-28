class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cnt = 0
        signal = 0
        sign = [1,-1] # +, -
        value = arr[0]
        temp = 0
        ans = 0
        for i in range(len(arr)-1):
            j = i+1
            value = arr[i] - arr[j]
            if value < 0:
                signal = sign[1]
            elif value > 0:
                signal = sign[0]
            else:
                cnt = 0
                ans = max(cnt, ans)
                temp = 0
                continue

            if temp != signal:
                cnt += 1
            else:
                cnt = 1
            ans = max(cnt, ans)
            
            temp = signal
            value = arr[j]
        return ans+1
                
            
            