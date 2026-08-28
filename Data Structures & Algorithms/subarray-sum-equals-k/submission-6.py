class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curSum = 0
        mp = defaultdict(int)
        mp[0] = 1
        for i in range(len(nums)):
            curSum += nums[i]

            if curSum - k in mp:
                ans += mp[curSum - k]
            mp[curSum] += 1
        return ans