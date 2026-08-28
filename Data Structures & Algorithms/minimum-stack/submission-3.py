class MinStack:

    def __init__(self):
        self.stack = []
        self.substack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.substack.append(val)
        else:
            self.stack.append(val)
            minimum = self.substack[-1]
            if minimum > val:
                self.substack.append(val)
            else:
                self.substack.append(minimum)
        
    def pop(self) -> None:
        self.stack.pop()
        self.substack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.substack[-1]
