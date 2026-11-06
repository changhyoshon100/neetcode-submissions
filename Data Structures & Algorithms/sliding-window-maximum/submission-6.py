class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        L = 0
        for R in range(len(nums)):
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)

            if L > q[0]:
                q.popleft()
            
            if R - L + 1 >= k:
                ans.append(nums[q[0]])
                L += 1
            
        return ans


            