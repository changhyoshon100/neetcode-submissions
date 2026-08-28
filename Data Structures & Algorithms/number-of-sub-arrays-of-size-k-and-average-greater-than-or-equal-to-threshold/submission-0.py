class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        new_thr = threshold * k
        nums = 0
        cnt = 0
        for i in range(k):
            nums += arr[i]
        if nums >= new_thr:
            cnt = 1
        for i in range(k, len(arr)):
            # print(nums, arr[i], arr[i-k])
            nums = nums + arr[i] - arr[i-k]
            if nums >= new_thr:
                cnt += 1
        return cnt

            
