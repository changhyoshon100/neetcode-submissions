class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        paren = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []
        for i in range(len(s)):
            if s[i] not in paren:
                stack.append(s[i])
            else:
                close = paren[s[i]]
                if not stack:
                    return False
                if stack and close != stack.pop():
                    return False
        if stack:
            return False
        return True


