class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        total = 0
        cnt = 0
        mp[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            if total - k in mp:
                cnt += mp[total - k]
            mp[total] += 1
        return cnt