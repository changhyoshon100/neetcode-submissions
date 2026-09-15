class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True

        nums = str(x)
        L, R = 0, len(nums) - 1

        while L < R:
            if nums[L] != nums[R]:
                return False
            L += 1
            R -= 1

        return True