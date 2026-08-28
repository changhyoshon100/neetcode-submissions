class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                a,b = stack.pop(), stack.pop()
                val = a + b
                stack.append(val)
            elif t == '-':
                a,b = stack.pop(), stack.pop()
                val = b - a
                stack.append(val)
            elif t == '*':
                a,b = stack.pop(), stack.pop()
                val = a * b
                stack.append(val)
            elif t == '/':
                a,b = stack.pop(), stack.pop()
                val = int(b/a)
                stack.append(val)
            else:
                stack.append(int(t))
        return stack[0]