class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack = []
        for n in s:
            if n in mp:
                print(n)
                if not stack:
                    return False
                # print(stack)
                if stack.pop() != mp[n]: return False
            else:
                
                stack.append(n)
                
        return True if len(stack) == 0 else False
