'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None

class linked_list(object):
    def __init__(self):


class MinStack:
    # @param x, an integer
    # @return an integer
    list_a = []
    list_b = []

    def insert_into_min_stack(self,x):
        position = 0
        for i in range(0,len(self.list_b)):
            if x > i:
                position +=1

        self.list_b.insert(position, x)

    def delete_from_min_stack(self,x):
        position = 0
        for i in range(0,len(self.list_b)):
            if


    def push(self, x):
        self.list_a.append(x)
        self.insert_into_min_stack(x)



    # @return nothing
    def pop(self):
        self.delete_from_min_stack(x)

        return self.list_a.pop()



    # @return an integer
    def top(self):
        length = len(self.list_a)
        return self.list_a[length-1]

    # @return an integer
    def getMin(self):
        return 1


def main():
    m = MinStack()
    m.push(1)
    m.push(3)
    print(m.top())
    print(m.pop())
    print(m.top())

if __name__ == "__main__":
    main()
