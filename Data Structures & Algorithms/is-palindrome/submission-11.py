class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        filtered_s = ""
        for i in s:
            if i in 'qwertyuiopasdfghjklzxcvbnm' or i in '0123456789':
                filtered_s += i
        
        left, right = 0, len(filtered_s) - 1
        while left < right:
            if filtered_s[left] != filtered_s[right]:
                return False
            left += 1
            right -= 1
        return True