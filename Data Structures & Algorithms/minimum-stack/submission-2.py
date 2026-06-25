class MinStack:

    def __init__(self):
        self.vals = []
        self.mins = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if len(self.vals) == 1:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        self.vals.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.vals[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]