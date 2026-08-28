class Solution:
    def isValid(self, s: str) -> bool:
        cnt = 0
        valid_pairs = {
            ')':'(',
            '}':'{', 
            ']':'['
        }
        stack = []
        for i in range(len(s)):
            if s[i] in valid_pairs:
                cnt -= 1
                if stack and valid_pairs[s[i]] != stack.pop():
                    return False
            else:
                cnt += 1
                stack.append(s[i])
        if cnt != 0 or len(stack) != 0:
            return False
        return True