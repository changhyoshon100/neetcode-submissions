class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        mp = {
            ')':'(', 
            '}':'{',
            ']':'['       
        }
        for i in range(len(s)):
            if s[i] in mp:
                if not stack: return False
                if mp[s[i]] != stack.pop():
                    return False
            else:
                stack.append(s[i])
        
        return True if not stack else False

