'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class stack:
    def __init__(self):
        self.data = []

    def push(self,x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def top(self):
        length = len(self.data)
        if length > 0:
            return self.data[length-1]
        else:
            return None


class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.data_stack = stack()
        self.min_stack = stack()
    def push(self, x):
        self.data_stack.push(x)
        if x<= self.min_stack.top() or self.min_stack.top()==None:
            self.min_stack.push(x)


    # @return nothing
    def pop(self):
        x = self.data_stack.pop()
        if x == self.min_stack.top():
            self.min_stack.pop()

    # @return an integer
    def top(self):
        return self.data_stack.top()



    # @return an integer
    def getMin(self):
        return self.min_stack.top()


def main():

    s = MinStack()
    s.push(0)
    s.push(1)
    s.push(0)

    print s.getMin()
    s.pop()
    print s.getMin()
    #
    # s.pop()
    # s.pop()
    # print s.getMin()
    # s.pop()
    # print s.getMin()
    # s.push(-3)
    # print s.getMin()






if __name__ == "__main__":
    main()
