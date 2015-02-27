'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class node(object):
    def __init__(self, data):
        """

        :rtype : object
        """
        self.data = data
        self.next_node = None


class linked_list(object):
    def __init__(self):
        self.head = node(None)
        self.head.next_node = None

    def push(self, x):
        temp = node(x)
        temp.next_node = self.head
        self.head = temp

    @property
    def pop(self):
        temp = self.head
        head = self.head.next_node
        return temp.data

    def top(self):
        return self.head.data


    def print_list(self):
        temp = self.head
        while (temp.next_node):
            print temp.data,
            temp = temp.next_node




class special_linked_list(linked_list):
    def push(self,x):
        position = 0
        temp = self.head
        prev = self.head
        while (x > temp.data and temp.next_node):
            temp = temp.next_node
            prev = temp
        new_node = node(x)
        new_node.next_node = prev.next_node
        prev.next_node = new_node

    def remove(self,x):
        position = 0
        temp = self.head
        prev = self.head
        while (x > temp.data and temp.next_node):
            temp = temp.next_node
            prev = temp

        prev.next_node = temp.next_node



class MinStack:
    # @param x, an integer
    # @return an integer
    list_min  = special_linked_list()
    list_c = linked_list()



    #     for i in range(0,len(self.list_b)):
    #         if x > i:
    #             position +=1
    #
    #     self.list_b.insert(position, x)

    # def delete_from_min_stack(self,x):
    #     position = 0
    #     for i in range(0,len(self.list_b)):
    #         if


    def push(self, x):
        #self.list_a.append(x)
        #self.insert_into_min_stack(x)
        self.list_c.push(x)
        self.list_min.push(x)


    # @return nothing
    def pop(self):
        #self.delete_from_min_stack(x)
        x = self.list_c.pop
        self.list_min.remove(x)
        return x


    # @return an integer
    def top(self):
        #length = len(self.list_a)
        #return self.list_a[length-1]
        return self.list_c.top()


    # @return an integer
    def getMin(self):
        return 1

    def print_stack(self):
        self.list_c.print_list()


def main():
    m = MinStack()
    m.push(1)
    m.push(3)
    m.push(4)
    print(m.top())
    print(m.pop())
    print(m.top())
    m.print_stack()


if __name__ == "__main__":
    main()
