class MyStack:

    def __init__(self):
        self.q = deque()
        self.q_sub = deque()

    def push(self, x: int) -> None:
        self.q_sub.append(x)
        while self.q:
            self.q_sub.append(self.q.popleft())
        self.q, self.q_sub = self.q_sub, self.q

    def pop(self) -> int:
        if self.q:
            return self.q.popleft()
        else:
            return None

    def top(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return None

    def empty(self) -> bool:
        if self.q:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()