class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    # pop in general is O(1) but in some rare case is O(n) thus amortized is O(1)
    def pop(self) -> int:
        if len(self.output) == 0:
            while self.input:
                self.output.append(self.input.pop())
        
        return self.output.pop()

    # peek in general is O(1) but in some rare case is O(n) thus amortized is O(1)
    def peek(self) -> int:
        if len(self.output) == 0:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
