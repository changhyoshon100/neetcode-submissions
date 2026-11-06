class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini:
            self.mini.append(val)
        else:
            new_val = min(val, self.mini[-1])
            self.mini.append(new_val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
