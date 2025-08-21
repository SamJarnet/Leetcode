class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
        for i in range(0, 8):
            self.stack.append([])
            self.stack.append([])
        self.head = 0
        self.minhead = 0


    def push(self, val: int) -> None:
        if self.min[self.minhead] == []:
            self.min[self.minhead] = val
            self.minhead += 1
        if self.head < 8:
            self.stack[self.head] = val
            self.head += 1

    def pop(self) -> None:
        self.stack[self.head-1] = []
        self.head -= 1

    def top(self) -> int:
        return self.stack[self.head-1]

    def getMin(self) -> int:
        return minStack
    
    ## WIP

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
minStack.top()   # return 0
minStack.getMin() #return -2