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
        print ("Cons: Inserted {} with link{}".format(self.head.data, self.head.next_node))


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
    def top(self):
        return self.head.data

    def push(self, x):

        # special case for head end
        temp = node(x)
        if (self.head.next_node is None) or (self.head.data > temp.data):
            temp.next_node = self.head
            self.head = temp

        # for other cases
        else:
            current = self.head
            while (current.next_node and temp.data >= current.next_node.data):
                current = current.next_node
            temp.next_node = current.next_node
            current.next_node = temp

        #print ("Inserted {} with link{}".format(temp.data, temp.next_node))

    def remove(self,x):
        position = 0
        temp = self.head
        prev = self.head
        while (x > temp.data and temp.next_node):
            temp = temp.next_node
            prev = temp

        prev.next_node = temp.next_node

    def print_list(self):
        temp = self.head
        while (temp.next_node):
            print temp.data
            temp = temp.next_node



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
        return self.list_min.top()

    def print_stack(self):
        print("main stack")
        self.list_c.print_list()
        print("\nmin stack")
        self.list_min.print_list()


def main():
    m = MinStack()
    m.push(12)
    m.push(3)
    m.push(4)
    m.push(7)
    m.push(2)
    m.push(9)
    m.push(11)
    m.push(0)
    m.push(14   )
    m.push(13)
    m.push(5)
    m.push(-10)
    print(m.top())
    #print(m.pop())
    print(m.top())
    print(m.getMin())
    #m.print_stack()
    #print ("Min stack")
    m.print_stack()


if __name__ == "__main__":
    main()
