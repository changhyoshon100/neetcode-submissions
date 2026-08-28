class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ')':'(', 
            '}':'{',  
            ']':'['
        }
        stack = []
        
        cnt = len(s) / 2
        if int(cnt) < cnt:
            return False
        cnt = int(cnt)

        for i in range(len(s)):
            if s[i] in list(paren.values()):
                stack.append(s[i])
            else:
                if len(stack) > 0 and stack.pop() == paren[s[i]]:
                    continue
                else:
                    return False
        print(stack)
        if len(stack) != 0:
            return False
        else: return True

