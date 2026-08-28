class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        res = 0
        mp = defaultdict(int)
        mp[0] = 1
        for i in range(len(nums)):
            res += nums[i]

            if res - k in mp:
                ans += mp[res - k]
            mp[res] += 1
        return ans 
            