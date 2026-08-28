class MyStack:

    def __init__(self):
        self.queue = deque()
        self.subqueue = deque()
    def push(self, x: int) -> None:
        while self.queue:
            self.subqueue.append(self.queue.popleft())
        self.queue.append(x)
        while self.subqueue:
            self.queue.append(self.subqueue.popleft())
        
    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return True if not self.queue else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()