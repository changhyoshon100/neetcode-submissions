class MinStack:
    def __init__(self):
        self.stack = []
        self.small = []

    def push(self, val: int) -> None:
        self.newVal = val
        if self.stack:
            self.lastVal = self.small[-1]
            self.small.append(min(self.newVal, self.lastVal))
        else:
            self.small.append(self.newVal)
        self.stack.append(self.newVal)
        

    def pop(self) -> None:
        self.stack.pop()
        self.small.pop()

    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        print(self.small)
        if self.small:
            return self.small[-1]
        
        


        
