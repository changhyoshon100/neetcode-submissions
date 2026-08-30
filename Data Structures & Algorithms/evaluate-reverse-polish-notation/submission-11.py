class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if stack and t == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif stack and t == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif stack and t == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif stack and t == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
                
            else:
                stack.append(int(t))
        return stack[0]