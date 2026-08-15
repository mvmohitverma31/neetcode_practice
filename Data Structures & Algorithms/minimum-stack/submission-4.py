class MinStack:
    def __init__(self):
        self.stack=[]
        self.MinStack=[] 
    def push(self,val):
        self.stack.append(val)
        if self.MinStack==[]:
            self.MinStack.append(val)
        else:
            if self.stack[-1]<=self.MinStack[-1]:
                self.MinStack.append(self.stack[-1])
    def pop(self):
        p=self.stack.pop()
        if self.MinStack[-1]==p:
            self.MinStack.pop()

        return p
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.MinStack[-1]