class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        cnt = 10**9
        
        for R in range(len(nums)):
            total += nums[R]
            if total >= target:
               
                while total >= target:
                    total -= nums[L]
                    L += 1
                # print(total, nums[L])
                # total += nums[L]
                # L -= 1
                cnt = min(cnt, R - L + 1)

        return cnt +1 if cnt != 10**9 else 0
                
            
