class Solution:
    def isValid(self, s: str) -> bool:
        if int(len(s)/2) < len(s)/2:
            return False
        cnt = 0
        valid_pairs = {
            ')':'(',
            '}':'{', 
            ']':'['
        }
        stack = []
        for i in range(len(s)):
            print(stack)
            if s[i] in valid_pairs:
                cnt -= 1
                if stack and valid_pairs[s[i]] != stack[-1]:
                    return False
                elif stack and valid_pairs[s[i]] == stack[-1]:
                    stack.pop()
            else:
                cnt += 1
                stack.append(s[i])
        print(stack)
        if cnt != 0:
            return False
        if len(stack) == 0:
            return True
        else:
            return False
