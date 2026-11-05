class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()
        self.counter = 0 # if counter % 2 == 1, first queue holds info

    def push(self, x: int) -> None:
        if(self.counter % 2 == 0):
            self.first.append(x)
            while(len(self.second) > 0):
                self.first.append(self.second.popleft())
        else:
            self.second.append(x)
            while(len(self.first) > 0):
                self.second.append(self.first.popleft())
        self.counter += 1

    def pop(self) -> int:
        if(self.counter % 2 == 0):
            return self.second.popleft()
        return self.first.popleft()

    def top(self) -> int:
        if(self.counter % 2 == 0):
            return self.second[0]
        return self.first[0]

    def empty(self) -> bool:
        if(self.counter % 2 == 0):
            return (len(self.second) == 0)
        return len(self.first) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()