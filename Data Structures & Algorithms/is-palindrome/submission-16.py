class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        sentence = ""
        for ch in s:
            if ch.isalnum():
                sentence += ch
        left, right = 0, len(sentence) - 1

        while left < right:
            
            if sentence[left] != sentence[right]:
                return False
            left += 1
            right -= 1
        return True




