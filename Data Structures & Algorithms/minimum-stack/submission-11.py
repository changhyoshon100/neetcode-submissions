class MinStack:

    def __init__(self):
        self.stack = []
        self.small = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.small:
            self.small.append(min(self.small[-1], val))
        else:
            self.small.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.small.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.small[-1]
