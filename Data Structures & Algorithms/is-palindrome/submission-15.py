class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = ""
        for ch in s:
            if ch.isalnum():
                chars += ch

        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        return True
