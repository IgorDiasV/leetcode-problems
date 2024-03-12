class MinStack:

    def __init__(self):
        self.list_values = []

    def push(self, val: int) -> None:
        self.list_values.append(val)

    def pop(self) -> None:
        self.list_values.pop()
        

    def top(self) -> int:
        return self.list_values[-1]

    def getMin(self) -> int:
        return min(self.list_values)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()