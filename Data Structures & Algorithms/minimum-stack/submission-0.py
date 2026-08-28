class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
    def push(self, val: int) -> None:
        self.mini.append(val)
        self.mini.sort(reverse=True)
        self.stack.append(val)
    def pop(self) -> None:
        
        if self.stack:
            pop_val = self.stack[-1]        
            self.stack = self.stack[:-1]
        # if min_val == self.mini[0]:
        #     self.mini[:] = self.mini[1:]
        self.mini.remove(pop_val)
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]

        
