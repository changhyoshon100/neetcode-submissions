class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ')':'(', 
            '}':'{',
            ']':'['
        }
        stack = []
        for i in s:

            if i in hashMap:
                if not stack:
                    return False
                last = stack.pop()
                if last != hashMap[i]:
                    return False
            else:
                stack.append(i)
                
        if stack:
            return False
        return True
