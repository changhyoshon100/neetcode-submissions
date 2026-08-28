class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        storage = set()
        cnt = 0
        l = 0
        for i in range(len(s)):
            while s[i] in storage:
                
                storage.remove(s[l])
                l += 1

            storage.add(s[i])
            cnt = max(cnt, i - l + 1)
        return cnt
        
